"""
Modelo de Machine Learning para Predição de Doenças Genéticas

Utiliza um ensemble de modelos:
- Random Forest para classificação (desenvolve/não desenvolve)
- Gradient Boosting para regressão (probabilidade estimada)

Features utilizadas:
- Grau de parentesco e compartilhamento genético
- Tipo de herança da doença
- Penetrância da doença
- Sexo e idade do parente
- Fatores ambientais/estilo de vida
- Número de afetados na família
"""

import numpy as np
import pickle
import os

try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False

from sklearn.ensemble import RandomForestClassifier, GradientBoostingRegressor
from sklearn.preprocessing import LabelEncoder, StandardScaler

try:
    from sklearn.model_selection import train_test_split, cross_val_score
    from sklearn.metrics import (
        accuracy_score, precision_score, recall_score, f1_score,
        roc_auc_score, mean_absolute_error, classification_report
    )
except ImportError:
    pass

import warnings
warnings.filterwarnings('ignore')


class GeneticDiseasePredictor:
    """
    Preditor de doenças genéticas baseado em Machine Learning.
    
    Combina classificação binária (risco/sem risco) com
    regressão para estimar a probabilidade percentual.
    """

    def __init__(self):
        self.classifier = RandomForestClassifier(
            n_estimators=50,
            max_depth=10,
            min_samples_split=10,
            min_samples_leaf=4,
            random_state=42,
            class_weight='balanced',
            n_jobs=-1
        )
        self.regressor = GradientBoostingRegressor(
            n_estimators=80,
            max_depth=4,
            learning_rate=0.15,
            min_samples_split=10,
            min_samples_leaf=5,
            random_state=42
        )
        self.label_encoders = {}
        self.scaler = StandardScaler()
        self.feature_columns = None
        self.is_trained = False
        self.metrics = {}

    def _prepare_features(self, df, fit=False):
        """Prepara as features para o modelo."""
        # Colunas categóricas para encoding
        categorical_cols = ['tipo_heranca', 'categoria_doenca']

        # Colunas numéricas
        numeric_cols = [
            'grau_parentesco', 'compartilhamento_genetico', 'penetrancia',
            'sexo_parente', 'idade_parente', 'idade_afetado',
            'num_afetados_familia', 'tabagismo', 'alcoolismo',
            'sedentarismo', 'obesidade', 'exposicao_quimicos',
            'dieta_inadequada', 'estresse_cronico'
        ]

        df_processed = df.copy()

        # Encoding de variáveis categóricas
        for col in categorical_cols:
            if col in df_processed.columns:
                if fit:
                    self.label_encoders[col] = LabelEncoder()
                    df_processed[col + '_encoded'] = self.label_encoders[col].fit_transform(
                        df_processed[col].astype(str)
                    )
                else:
                    if col in self.label_encoders:
                        # Lidar com categorias não vistas
                        known_classes = set(self.label_encoders[col].classes_)
                        df_processed[col] = df_processed[col].apply(
                            lambda x: x if x in known_classes else self.label_encoders[col].classes_[0]
                        )
                        df_processed[col + '_encoded'] = self.label_encoders[col].transform(
                            df_processed[col].astype(str)
                        )

        # Feature engineering adicional
        df_processed['risco_idade'] = df_processed['idade_parente'] * df_processed['compartilhamento_genetico']
        df_processed['fatores_risco_total'] = (
            df_processed['tabagismo'] + df_processed['alcoolismo'] +
            df_processed['sedentarismo'] + df_processed['obesidade'] +
            df_processed['exposicao_quimicos'] + df_processed['dieta_inadequada'] +
            df_processed['estresse_cronico']
        )
        df_processed['interacao_genetica_ambiente'] = (
            df_processed['compartilhamento_genetico'] * df_processed['fatores_risco_total']
        )
        df_processed['familia_x_parentesco'] = (
            df_processed['num_afetados_familia'] * df_processed['compartilhamento_genetico']
        )

        # Selecionar features finais
        feature_cols = (
            numeric_cols +
            [col + '_encoded' for col in categorical_cols if col + '_encoded' in df_processed.columns] +
            ['risco_idade', 'fatores_risco_total', 'interacao_genetica_ambiente', 'familia_x_parentesco']
        )

        if fit:
            self.feature_columns = feature_cols

        X = df_processed[self.feature_columns].values

        if fit:
            X = self.scaler.fit_transform(X)
        else:
            X = self.scaler.transform(X)

        return X

    def train(self, df):
        """Treina o modelo com o dataset fornecido."""
        print("Preparando features...")
        X = self._prepare_features(df, fit=True)
        y_class = df['desenvolve_doenca'].values
        y_prob = df['probabilidade_calculada'].values

        # Split treino/teste
        X_train, X_test, y_class_train, y_class_test, y_prob_train, y_prob_test = train_test_split(
            X, y_class, y_prob, test_size=0.2, random_state=42, stratify=y_class
        )

        print(f"Amostras de treino: {len(X_train)}")
        print(f"Amostras de teste: {len(X_test)}")

        # Treinar classificador
        print("\nTreinando classificador (Random Forest)...")
        self.classifier.fit(X_train, y_class_train)
        y_class_pred = self.classifier.predict(X_test)
        y_class_proba = self.classifier.predict_proba(X_test)[:, 1]

        # Treinar regressor
        print("Treinando regressor (Gradient Boosting)...")
        self.regressor.fit(X_train, y_prob_train)
        y_prob_pred = self.regressor.predict(X_test)

        # Calcular métricas
        self.metrics = {
            "classificacao": {
                "accuracy": round(accuracy_score(y_class_test, y_class_pred), 4),
                "precision": round(precision_score(y_class_test, y_class_pred, zero_division=0), 4),
                "recall": round(recall_score(y_class_test, y_class_pred, zero_division=0), 4),
                "f1_score": round(f1_score(y_class_test, y_class_pred, zero_division=0), 4),
                "roc_auc": round(roc_auc_score(y_class_test, y_class_proba), 4),
            },
            "regressao": {
                "mae": round(mean_absolute_error(y_prob_test, y_prob_pred), 4),
                "correlacao": round(np.corrcoef(y_prob_test, y_prob_pred)[0, 1], 4),
            }
        }

        # Cross-validation
        cv_scores = cross_val_score(self.classifier, X, y_class, cv=5, scoring='roc_auc')
        self.metrics["cross_validation_auc"] = round(cv_scores.mean(), 4)

        # Feature importance
        feature_importance = dict(zip(
            self.feature_columns,
            self.classifier.feature_importances_
        ))
        self.metrics["top_features"] = dict(
            sorted(feature_importance.items(), key=lambda x: x[1], reverse=True)[:10]
        )

        self.is_trained = True

        print("\n=== MÉTRICAS DO MODELO ===")
        print(f"Acurácia: {self.metrics['classificacao']['accuracy']}")
        print(f"Precision: {self.metrics['classificacao']['precision']}")
        print(f"Recall: {self.metrics['classificacao']['recall']}")
        print(f"F1-Score: {self.metrics['classificacao']['f1_score']}")
        print(f"ROC-AUC: {self.metrics['classificacao']['roc_auc']}")
        print(f"Cross-val AUC: {self.metrics['cross_validation_auc']}")
        print(f"MAE (regressão): {self.metrics['regressao']['mae']}")

        print("\nTop 5 Features mais importantes:")
        for feat, imp in list(self.metrics["top_features"].items())[:5]:
            print(f"  {feat}: {imp:.4f}")

        return self.metrics

    def predict(self, dados_entrada):
        """
        Faz predição para um novo caso.
        
        Args:
            dados_entrada: dict com as features do caso
            
        Returns:
            dict com probabilidade, classificação e nível de risco
        """
        if not self.is_trained:
            raise ValueError("Modelo não treinado. Execute train() primeiro.")

        # Preparar features sem pandas
        X = self._prepare_single_input(dados_entrada)

        # Predição de classificação
        prob_classe = self.classifier.predict_proba(X)[0]
        classificacao = self.classifier.predict(X)[0]

        # Predição de probabilidade
        prob_regressao = self.regressor.predict(X)[0]
        prob_regressao = max(0.01, min(0.99, prob_regressao))

        # Combinar predições (média ponderada)
        prob_final = 0.4 * prob_classe[1] + 0.6 * prob_regressao
        prob_final = max(0.01, min(0.99, prob_final))

        # Classificar nível de risco
        if prob_final < 0.10:
            nivel_risco = "Muito Baixo"
            cor_risco = "#28a745"
        elif prob_final < 0.25:
            nivel_risco = "Baixo"
            cor_risco = "#7bc67e"
        elif prob_final < 0.45:
            nivel_risco = "Moderado"
            cor_risco = "#ffc107"
        elif prob_final < 0.65:
            nivel_risco = "Alto"
            cor_risco = "#fd7e14"
        else:
            nivel_risco = "Muito Alto"
            cor_risco = "#dc3545"

        # Gerar recomendações
        recomendacoes = self._gerar_recomendacoes(dados_entrada, prob_final, nivel_risco)

        resultado = {
            "probabilidade": round(prob_final * 100, 2),
            "classificacao": int(classificacao),
            "nivel_risco": nivel_risco,
            "cor_risco": cor_risco,
            "confianca_modelo": round(max(prob_classe) * 100, 1),
            "prob_classificador": round(prob_classe[1] * 100, 2),
            "prob_regressor": round(prob_regressao * 100, 2),
            "recomendacoes": recomendacoes,
        }

        return resultado

    def _prepare_single_input(self, dados):
        """Prepara um único input para predição sem usar pandas."""
        categorical_cols = ['tipo_heranca', 'categoria_doenca']
        numeric_cols = [
            'grau_parentesco', 'compartilhamento_genetico', 'penetrancia',
            'sexo_parente', 'idade_parente', 'idade_afetado',
            'num_afetados_familia', 'tabagismo', 'alcoolismo',
            'sedentarismo', 'obesidade', 'exposicao_quimicos',
            'dieta_inadequada', 'estresse_cronico'
        ]

        features = []

        # Colunas numéricas
        for col in numeric_cols:
            features.append(float(dados.get(col, 0)))

        # Colunas categóricas encoded
        for col in categorical_cols:
            if col in self.label_encoders:
                val = str(dados.get(col, ''))
                known_classes = set(self.label_encoders[col].classes_)
                if val not in known_classes:
                    val = self.label_encoders[col].classes_[0]
                encoded = self.label_encoders[col].transform([val])[0]
                features.append(float(encoded))

        # Feature engineering
        idade_parente = float(dados.get('idade_parente', 0))
        compartilhamento = float(dados.get('compartilhamento_genetico', 0))
        num_afetados = float(dados.get('num_afetados_familia', 1))

        risco_idade = idade_parente * compartilhamento
        fatores_risco_total = sum([
            float(dados.get('tabagismo', 0)),
            float(dados.get('alcoolismo', 0)),
            float(dados.get('sedentarismo', 0)),
            float(dados.get('obesidade', 0)),
            float(dados.get('exposicao_quimicos', 0)),
            float(dados.get('dieta_inadequada', 0)),
            float(dados.get('estresse_cronico', 0)),
        ])
        interacao_genetica_ambiente = compartilhamento * fatores_risco_total
        familia_x_parentesco = num_afetados * compartilhamento

        features.extend([risco_idade, fatores_risco_total, interacao_genetica_ambiente, familia_x_parentesco])

        X = np.array([features])
        X = self.scaler.transform(X)
        return X

    def _gerar_recomendacoes(self, dados, prob, nivel_risco):
        """Gera recomendações baseadas no resultado."""
        recomendacoes = []

        if nivel_risco in ["Alto", "Muito Alto"]:
            recomendacoes.append("Consultar um geneticista clínico para aconselhamento genético detalhado.")
            recomendacoes.append("Considerar realização de testes genéticos específicos para a doença.")
            recomendacoes.append("Estabelecer um plano de monitoramento e rastreamento precoce.")

        if nivel_risco == "Moderado":
            recomendacoes.append("Agendar consulta com geneticista para avaliação de risco personalizada.")
            recomendacoes.append("Manter acompanhamento médico regular com exames periódicos.")

        if nivel_risco in ["Baixo", "Muito Baixo"]:
            recomendacoes.append("Manter rotina de exames preventivos regulares.")
            recomendacoes.append("Informar histórico familiar ao médico em consultas de rotina.")

        # Recomendações baseadas em fatores de risco
        if dados.get("tabagismo", 0) == 1:
            recomendacoes.append("Cessar tabagismo - fator de risco modificável importante.")
        if dados.get("sedentarismo", 0) == 1:
            recomendacoes.append("Iniciar programa de atividade física regular.")
        if dados.get("obesidade", 0) == 1:
            recomendacoes.append("Buscar orientação nutricional para controle de peso.")
        if dados.get("alcoolismo", 0) == 1:
            recomendacoes.append("Reduzir ou eliminar consumo de álcool.")

        recomendacoes.append(
            "IMPORTANTE: Este sistema é apenas uma ferramenta de estimativa. "
            "Sempre consulte profissionais de saúde qualificados para decisões médicas."
        )

        return recomendacoes

    def save_model(self, path):
        """Salva o modelo treinado em disco."""
        model_data = {
            'classifier': self.classifier,
            'regressor': self.regressor,
            'label_encoders': self.label_encoders,
            'scaler': self.scaler,
            'feature_columns': self.feature_columns,
            'metrics': self.metrics,
            'is_trained': self.is_trained,
        }
        with open(path, 'wb') as f:
            pickle.dump(model_data, f)
        print(f"Modelo salvo em: {path}")

    def load_model(self, path):
        """Carrega modelo treinado do disco."""
        with open(path, 'rb') as f:
            model_data = pickle.load(f)

        self.classifier = model_data['classifier']
        self.regressor = model_data['regressor']
        self.label_encoders = model_data['label_encoders']
        self.scaler = model_data['scaler']
        self.feature_columns = model_data['feature_columns']
        self.metrics = model_data['metrics']
        self.is_trained = model_data['is_trained']
        print(f"Modelo carregado de: {path}")


def train_and_save():
    """Treina o modelo e salva em disco."""
    # Importar e gerar dataset
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'data'))
    from generate_dataset import gerar_dataset, salvar_metadados

    print("=" * 60)
    print("TREINAMENTO DO MODELO DE PREDIÇÃO DE DOENÇAS GENÉTICAS")
    print("=" * 60)

    # Gerar dataset
    print("\n1. Gerando dataset sintético...")
    df = gerar_dataset(n_amostras=10000)
    print(f"   Dataset gerado com {len(df)} amostras")

    # Salvar dataset
    dataset_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'dataset_genetico.csv')
    df.to_csv(dataset_path, index=False)
    print(f"   Dataset salvo em: {dataset_path}")

    # Salvar metadados
    salvar_metadados()

    # Treinar modelo
    print("\n2. Treinando modelo...")
    predictor = GeneticDiseasePredictor()
    metrics = predictor.train(df)

    # Salvar modelo
    model_path = os.path.join(os.path.dirname(__file__), 'trained_model.pkl')
    predictor.save_model(model_path)

    # Teste rápido
    print("\n3. Teste de predição...")
    teste = {
        'tipo_heranca': 'autossomica_dominante',
        'categoria_doenca': 'doenca_rara',
        'grau_parentesco': 1,
        'compartilhamento_genetico': 0.50,
        'penetrancia': 0.95,
        'sexo_parente': 1,
        'idade_parente': 35,
        'idade_afetado': 60,
        'num_afetados_familia': 2,
        'tabagismo': 0,
        'alcoolismo': 0,
        'sedentarismo': 0,
        'obesidade': 0,
        'exposicao_quimicos': 0,
        'dieta_inadequada': 0,
        'estresse_cronico': 0,
    }

    resultado = predictor.predict(teste)
    print(f"\n   Caso teste (Filho, doença autossômica dominante):")
    print(f"   Probabilidade: {resultado['probabilidade']}%")
    print(f"   Nível de risco: {resultado['nivel_risco']}")
    print(f"   Confiança do modelo: {resultado['confianca_modelo']}%")

    print("\n" + "=" * 60)
    print("TREINAMENTO CONCLUÍDO COM SUCESSO!")
    print("=" * 60)

    return predictor


if __name__ == "__main__":
    train_and_save()
