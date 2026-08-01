"""
API Flask para o Sistema de Predição de Doenças Genéticas

Endpoints:
- POST /api/predict - Faz predição de risco genético
- GET /api/diseases - Lista doenças disponíveis
- GET /api/relationships - Lista parentescos disponíveis
- GET /api/model-info - Informações sobre o modelo
"""

import os
import sys
import json
import numpy as np
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

# Adicionar diretórios ao path
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'models'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'data'))

from models.genetic_predictor import GeneticDiseasePredictor
from data.generate_dataset import DOENCAS, PARENTESCOS
from data.disease_info import DISEASE_CLINICAL_INFO, get_urgency_level, get_urgency_description

app = Flask(__name__, static_folder='../frontend')
CORS(app)

# Variável global para o modelo
predictor = None


def get_predictor():
    """Carrega ou treina o modelo."""
    global predictor
    if predictor is not None and predictor.is_trained:
        return predictor

    model_path = os.path.join(os.path.dirname(__file__), 'models', 'trained_model.pkl')

    predictor = GeneticDiseasePredictor()

    if os.path.exists(model_path):
        try:
            predictor.load_model(model_path)
            print("Modelo carregado do cache.")
        except Exception as e:
            print(f"Erro ao carregar modelo: {e}. Treinando novo modelo sem pandas...")
            predictor = train_without_pandas()
    else:
        print("Modelo não encontrado. Treinando novo modelo...")
        predictor = train_without_pandas()

    return predictor


def train_without_pandas():
    """Treina o modelo sem depender de pandas, usando numpy puro."""
    from data.generate_dataset import (
        DOENCAS, PARENTESCOS, calcular_probabilidade_base,
        gerar_fatores_ambientais, ajustar_probabilidade_por_fatores
    )

    np.random.seed(42)
    n_amostras = 8000

    # Gerar dados como listas
    all_features = []
    all_labels_class = []
    all_labels_prob = []

    doenca_ids = list(DOENCAS.keys())
    parentesco_ids = list(PARENTESCOS.keys())
    parentescos_femininos = ["mae", "filha", "irma", "avo_materna", "tia", "sobrinha", "prima", "meia_irma"]
    parentescos_masculinos = ["pai", "filho", "irmao", "avo_paterno", "tio", "sobrinho", "primo", "meio_irmao"]

    # Tipo heranca -> indice
    tipos_heranca = sorted(set(d["tipo_heranca"] for d in DOENCAS.values()))
    categorias = sorted(set(d["categoria"] for d in DOENCAS.values()))

    for _ in range(n_amostras):
        doenca_id = np.random.choice(doenca_ids)
        doenca_info = DOENCAS[doenca_id]
        parentesco_id = np.random.choice(parentesco_ids)
        parentesco_info = PARENTESCOS[parentesco_id]

        if parentesco_id in parentescos_femininos:
            sexo_parente = 0
        elif parentesco_id in parentescos_masculinos:
            sexo_parente = 1
        else:
            sexo_parente = np.random.choice([0, 1])

        idade_parente = np.random.randint(1, 85)
        idade_afetado = np.random.randint(1, 85)
        num_afetados = np.random.choice([1, 2, 3, 4, 5], p=[0.40, 0.30, 0.15, 0.10, 0.05])
        fatores = gerar_fatores_ambientais()

        sexo_str = "masculino" if sexo_parente == 1 else "feminino"
        prob_base = calcular_probabilidade_base(doenca_info, parentesco_info, sexo_str)
        prob_ajustada = ajustar_probabilidade_por_fatores(prob_base, fatores, doenca_info)
        prob_ajustada = min(prob_ajustada * (1.0 + (num_afetados - 1) * 0.10), 0.99)

        # Ajuste por idade
        if doenca_id in ["huntington", "cancer_mama_brca1", "cancer_mama_brca2",
                         "cancer_prostata", "melanoma_familiar", "sindrome_lynch",
                         "alzheimer_familiar", "parkinson_familiar", "ela_familiar",
                         "cancer_pancreas_hereditario", "cancer_estomago_difuso",
                         "cancer_endometrio", "cancer_pulmao_hereditario",
                         "cancer_bexiga_hereditario", "diabetes_tipo2_genetico",
                         "hipercolesterolemia_familiar", "cardiomiopatia_hipertrofica",
                         "esquizofrenia", "transtorno_bipolar",
                         "artrite_reumatoide", "lupus", "esclerose_multipla"]:
            if idade_parente < 20:
                prob_ajustada *= 0.3
            elif idade_parente < 40:
                prob_ajustada *= 0.7
            elif idade_parente >= 60:
                prob_ajustada *= 1.1
            prob_ajustada = min(prob_ajustada, 0.99)

        desenvolve = 1 if np.random.random() < prob_ajustada else 0
        prob_final = max(0.01, min(0.99, prob_ajustada + np.random.normal(0, 0.02)))

        # Features numéricas
        features = [
            parentesco_info["grau"],
            parentesco_info["compartilhamento_genetico"],
            doenca_info["penetrancia"],
            sexo_parente,
            idade_parente,
            idade_afetado,
            num_afetados,
            fatores["tabagismo"],
            fatores["alcoolismo"],
            fatores["sedentarismo"],
            fatores["obesidade"],
            fatores["exposicao_quimicos"],
            fatores["dieta_inadequada"],
            fatores["estresse_cronico"],
            # Encoded categoricals
            tipos_heranca.index(doenca_info["tipo_heranca"]),
            categorias.index(doenca_info["categoria"]),
            # Engineered features
            idade_parente * parentesco_info["compartilhamento_genetico"],  # risco_idade
            sum([fatores["tabagismo"], fatores["alcoolismo"], fatores["sedentarismo"],
                 fatores["obesidade"], fatores["exposicao_quimicos"],
                 fatores["dieta_inadequada"], fatores["estresse_cronico"]]),  # fatores_total
            parentesco_info["compartilhamento_genetico"] * sum([
                fatores["tabagismo"], fatores["alcoolismo"], fatores["sedentarismo"],
                fatores["obesidade"], fatores["exposicao_quimicos"],
                fatores["dieta_inadequada"], fatores["estresse_cronico"]]),  # interacao
            num_afetados * parentesco_info["compartilhamento_genetico"],  # familia_x_parentesco
        ]

        all_features.append(features)
        all_labels_class.append(desenvolve)
        all_labels_prob.append(prob_final)

    X = np.array(all_features, dtype=np.float64)
    y_class = np.array(all_labels_class)
    y_prob = np.array(all_labels_prob)

    # Criar e treinar predictor
    pred = GeneticDiseasePredictor()

    # Configurar label encoders manualmente
    from sklearn.preprocessing import LabelEncoder
    le_heranca = LabelEncoder()
    le_heranca.classes_ = np.array(tipos_heranca)
    le_cat = LabelEncoder()
    le_cat.classes_ = np.array(categorias)
    pred.label_encoders = {'tipo_heranca': le_heranca, 'categoria_doenca': le_cat}

    # Feature columns
    pred.feature_columns = [
        'grau_parentesco', 'compartilhamento_genetico', 'penetrancia',
        'sexo_parente', 'idade_parente', 'idade_afetado',
        'num_afetados_familia', 'tabagismo', 'alcoolismo',
        'sedentarismo', 'obesidade', 'exposicao_quimicos',
        'dieta_inadequada', 'estresse_cronico',
        'tipo_heranca_encoded', 'categoria_doenca_encoded',
        'risco_idade', 'fatores_risco_total', 'interacao_genetica_ambiente', 'familia_x_parentesco'
    ]

    # Fit scaler
    pred.scaler.fit(X)
    X_scaled = pred.scaler.transform(X)

    # Treinar modelos
    pred.classifier.fit(X_scaled, y_class)
    pred.regressor.fit(X_scaled, y_prob)
    pred.is_trained = True
    pred.metrics = {"info": "Treinado sem pandas no servidor"}

    # Salvar para cache
    model_path = os.path.join(os.path.dirname(__file__), 'models', 'trained_model.pkl')
    pred.save_model(model_path)

    print("Modelo treinado e salvo com sucesso (sem pandas)!")
    return pred


@app.route('/')
def index():
    """Serve a página principal."""
    return send_from_directory('../frontend', 'index.html')


@app.route('/static/<path:filename>')
def serve_static(filename):
    """Serve arquivos estáticos."""
    return send_from_directory('../frontend/static', filename)


@app.route('/api/predict', methods=['POST'])
def predict():
    """
    Endpoint principal de predição.
    
    Recebe dados do parente afetado e do parente a ser avaliado,
    retorna a probabilidade estimada de desenvolver a doença.
    """
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Dados não fornecidos"}), 400

        # Validar campos obrigatórios
        campos_obrigatorios = [
            'doenca_id', 'parentesco', 'sexo_parente',
            'idade_parente', 'idade_afetado'
        ]

        for campo in campos_obrigatorios:
            if campo not in data:
                return jsonify({"error": f"Campo obrigatório ausente: {campo}"}), 400

        # Obter informações da doença
        doenca_id = data['doenca_id']
        if doenca_id not in DOENCAS:
            return jsonify({"error": f"Doença não encontrada: {doenca_id}"}), 400

        doenca_info = DOENCAS[doenca_id]

        # Obter informações do parentesco
        parentesco = data['parentesco']
        if parentesco not in PARENTESCOS:
            return jsonify({"error": f"Parentesco não encontrado: {parentesco}"}), 400

        parentesco_info = PARENTESCOS[parentesco]

        # Montar dados para predição
        dados_predicao = {
            'tipo_heranca': doenca_info['tipo_heranca'],
            'categoria_doenca': doenca_info['categoria'],
            'grau_parentesco': parentesco_info['grau'],
            'compartilhamento_genetico': parentesco_info['compartilhamento_genetico'],
            'penetrancia': doenca_info['penetrancia'],
            'sexo_parente': int(data['sexo_parente']),
            'idade_parente': int(data['idade_parente']),
            'idade_afetado': int(data['idade_afetado']),
            'num_afetados_familia': int(data.get('num_afetados_familia', 1)),
            'tabagismo': int(data.get('tabagismo', 0)),
            'alcoolismo': int(data.get('alcoolismo', 0)),
            'sedentarismo': int(data.get('sedentarismo', 0)),
            'obesidade': int(data.get('obesidade', 0)),
            'exposicao_quimicos': int(data.get('exposicao_quimicos', 0)),
            'dieta_inadequada': int(data.get('dieta_inadequada', 0)),
            'estresse_cronico': int(data.get('estresse_cronico', 0)),
        }

        # Fazer predição
        model = get_predictor()
        resultado = model.predict(dados_predicao)

        # Adicionar informações contextuais
        resultado['doenca_info'] = {
            'nome': doenca_info['nome'],
            'tipo_heranca': doenca_info['tipo_heranca'],
            'categoria': doenca_info['categoria'],
            'penetrancia': doenca_info['penetrancia'],
        }
        resultado['parentesco_info'] = {
            'parentesco': parentesco,
            'grau': parentesco_info['grau'],
            'compartilhamento_genetico': parentesco_info['compartilhamento_genetico'],
        }

        # Adicionar informações clínicas (exames, especialistas, urgência)
        nivel_risco = resultado['nivel_risco']
        urgency = get_urgency_level(doenca_id, nivel_risco)
        urgency_desc = get_urgency_description(urgency)

        clinical = DISEASE_CLINICAL_INFO.get(doenca_id, {})
        resultado['clinical_info'] = {
            'exames': clinical.get('exames', []),
            'especialistas': clinical.get('especialistas', []),
            'nota_clinica': clinical.get('nota_clinica', ''),
            'urgencia': urgency,
            'urgencia_label': urgency_desc['label'],
            'urgencia_descricao': urgency_desc['descricao'],
            'urgencia_cor': urgency_desc['cor'],
            'urgencia_icone': urgency_desc['icone'],
        }

        return jsonify(resultado)

    except Exception as e:
        return jsonify({"error": f"Erro na predição: {str(e)}"}), 500


@app.route('/api/diseases', methods=['GET'])
def get_diseases():
    """Retorna lista de doenças disponíveis."""
    doencas_lista = []
    for doenca_id, info in DOENCAS.items():
        doencas_lista.append({
            "id": doenca_id,
            "nome": info["nome"],
            "tipo_heranca": info["tipo_heranca"],
            "categoria": info["categoria"],
            "penetrancia": info["penetrancia"],
            "tem_info_clinica": doenca_id in DISEASE_CLINICAL_INFO,
        })

    # Ordenar por categoria e nome
    doencas_lista.sort(key=lambda x: (x["categoria"], x["nome"]))
    return jsonify(doencas_lista)


@app.route('/api/relationships', methods=['GET'])
def get_relationships():
    """Retorna lista de parentescos disponíveis."""
    parentescos_lista = []
    for parentesco_id, info in PARENTESCOS.items():
        parentescos_lista.append({
            "id": parentesco_id,
            "label": parentesco_id.replace("_", " ").title(),
            "grau": info["grau"],
            "compartilhamento_genetico": info["compartilhamento_genetico"],
            "tipo": info["tipo"],
        })

    # Ordenar por grau
    parentescos_lista.sort(key=lambda x: (x["grau"], x["label"]))
    return jsonify(parentescos_lista)


@app.route('/api/model-info', methods=['GET'])
def get_model_info():
    """Retorna informações sobre o modelo treinado."""
    try:
        model = get_predictor()
        return jsonify({
            "is_trained": model.is_trained,
            "metrics": model.metrics,
            "features": model.feature_columns,
            "num_diseases": len(DOENCAS),
            "num_relationships": len(PARENTESCOS),
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/inheritance-info', methods=['GET'])
def get_inheritance_info():
    """Retorna informações sobre tipos de herança genética."""
    info = {
        "autossomica_dominante": {
            "nome": "Autossômica Dominante",
            "descricao": "Basta uma cópia do gene alterado para manifestar a doença. Cada filho tem 50% de chance de herdar.",
            "exemplos": ["Doença de Huntington", "Neurofibromatose", "Retinoblastoma"]
        },
        "autossomica_recessiva": {
            "nome": "Autossômica Recessiva",
            "descricao": "São necessárias duas cópias do gene alterado. Portadores não manifestam sintomas.",
            "exemplos": ["Fibrose Cística", "Anemia Falciforme", "Fenilcetonúria"]
        },
        "ligada_x_recessiva": {
            "nome": "Ligada ao X Recessiva",
            "descricao": "Gene no cromossomo X. Homens são mais afetados pois têm apenas um X.",
            "exemplos": ["Hemofilia A", "Distrofia de Duchenne"]
        },
        "multifatorial_dominante": {
            "nome": "Multifatorial com Componente Dominante",
            "descricao": "Combinação de predisposição genética com fatores ambientais. Mutação dominante com penetrância variável.",
            "exemplos": ["Câncer de Mama (BRCA)", "Síndrome de Lynch", "Melanoma Familiar"]
        }
    }
    return jsonify(info)


@app.route('/api/disease-info/<doenca_id>', methods=['GET'])
def get_disease_clinical_info(doenca_id):
    """Retorna informações clínicas detalhadas de uma doença."""
    if doenca_id not in DOENCAS:
        return jsonify({"error": f"Doença não encontrada: {doenca_id}"}), 404

    doenca_info = DOENCAS[doenca_id]
    clinical = DISEASE_CLINICAL_INFO.get(doenca_id, {})

    return jsonify({
        "id": doenca_id,
        "nome": doenca_info['nome'],
        "categoria": doenca_info['categoria'],
        "tipo_heranca": doenca_info['tipo_heranca'],
        "penetrancia": doenca_info['penetrancia'],
        "exames": clinical.get('exames', []),
        "especialistas": clinical.get('especialistas', []),
        "nota_clinica": clinical.get('nota_clinica', ''),
        "urgencia_por_risco": clinical.get('urgencia_por_risco', {}),
    })


if __name__ == '__main__':
    print("Inicializando Sistema de Predição de Doenças Genéticas...")
    print("Carregando modelo...")

    # Pré-carregar modelo
    get_predictor()

    print("\nServidor iniciado!")
    print("Acesse: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
