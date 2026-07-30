"""
Gerador de Dataset Sintético para Predição de Doenças Genéticas

Este módulo gera dados sintéticos baseados em padrões reais de herança genética,
incluindo:
- Herança autossômica dominante (ex: Doença de Huntington, alguns cânceres hereditários)
- Herança autossômica recessiva (ex: Fibrose Cística, Anemia Falciforme)
- Herança ligada ao X (ex: Hemofilia, Distrofia Muscular de Duchenne)
- Herança multifatorial (ex: Câncer de mama BRCA1/2, Diabetes tipo 2)

Fatores considerados:
- Grau de parentesco
- Tipo de herança da doença
- Sexo do parente
- Idade
- Fatores ambientais/estilo de vida
- Penetrância da doença
"""

import numpy as np
import pandas as pd
import json
import os

# Seed para reprodutibilidade
np.random.seed(42)

# ============================================================
# DEFINIÇÃO DAS DOENÇAS E SEUS PADRÕES DE HERANÇA
# ============================================================

DOENCAS = {
    # Doenças autossômicas dominantes
    "huntington": {
        "nome": "Doença de Huntington",
        "tipo_heranca": "autossomica_dominante",
        "penetrancia": 0.95,
        "categoria": "doenca_rara"
    },
    "retinoblastoma": {
        "nome": "Retinoblastoma Hereditário",
        "tipo_heranca": "autossomica_dominante",
        "penetrancia": 0.90,
        "categoria": "cancer"
    },
    "neurofibromatose": {
        "nome": "Neurofibromatose tipo 1",
        "tipo_heranca": "autossomica_dominante",
        "penetrancia": 0.95,
        "categoria": "doenca_rara"
    },
    "sindrome_lynch": {
        "nome": "Síndrome de Lynch (Câncer Colorretal Hereditário)",
        "tipo_heranca": "autossomica_dominante",
        "penetrancia": 0.80,
        "categoria": "cancer"
    },

    # Doenças autossômicas recessivas
    "fibrose_cistica": {
        "nome": "Fibrose Cística",
        "tipo_heranca": "autossomica_recessiva",
        "penetrancia": 0.99,
        "categoria": "doenca_rara"
    },
    "anemia_falciforme": {
        "nome": "Anemia Falciforme",
        "tipo_heranca": "autossomica_recessiva",
        "penetrancia": 0.99,
        "categoria": "doenca_rara"
    },
    "fenilcetonuria": {
        "nome": "Fenilcetonúria",
        "tipo_heranca": "autossomica_recessiva",
        "penetrancia": 0.99,
        "categoria": "doenca_rara"
    },

    # Doenças ligadas ao X
    "hemofilia_a": {
        "nome": "Hemofilia A",
        "tipo_heranca": "ligada_x_recessiva",
        "penetrancia": 0.99,
        "categoria": "doenca_rara"
    },
    "duchenne": {
        "nome": "Distrofia Muscular de Duchenne",
        "tipo_heranca": "ligada_x_recessiva",
        "penetrancia": 0.99,
        "categoria": "doenca_rara"
    },

    # Doenças multifatoriais / Cânceres hereditários
    "cancer_mama_brca1": {
        "nome": "Câncer de Mama (BRCA1)",
        "tipo_heranca": "multifatorial_dominante",
        "penetrancia": 0.72,
        "categoria": "cancer"
    },
    "cancer_mama_brca2": {
        "nome": "Câncer de Mama (BRCA2)",
        "tipo_heranca": "multifatorial_dominante",
        "penetrancia": 0.69,
        "categoria": "cancer"
    },
    "cancer_ovario_brca": {
        "nome": "Câncer de Ovário (BRCA1/2)",
        "tipo_heranca": "multifatorial_dominante",
        "penetrancia": 0.44,
        "categoria": "cancer"
    },
    "cancer_prostata": {
        "nome": "Câncer de Próstata Hereditário",
        "tipo_heranca": "multifatorial_dominante",
        "penetrancia": 0.60,
        "categoria": "cancer"
    },
    "melanoma_familiar": {
        "nome": "Melanoma Familiar (CDKN2A)",
        "tipo_heranca": "multifatorial_dominante",
        "penetrancia": 0.58,
        "categoria": "cancer"
    },
}

# ============================================================
# GRAUS DE PARENTESCO E COMPARTILHAMENTO GENÉTICO
# ============================================================

PARENTESCOS = {
    "pai": {"grau": 1, "compartilhamento_genetico": 0.50, "tipo": "progenitor"},
    "mae": {"grau": 1, "compartilhamento_genetico": 0.50, "tipo": "progenitor"},
    "filho": {"grau": 1, "compartilhamento_genetico": 0.50, "tipo": "descendente"},
    "filha": {"grau": 1, "compartilhamento_genetico": 0.50, "tipo": "descendente"},
    "irmao": {"grau": 1, "compartilhamento_genetico": 0.50, "tipo": "irmao"},
    "irma": {"grau": 1, "compartilhamento_genetico": 0.50, "tipo": "irmao"},
    "avo_paterno": {"grau": 2, "compartilhamento_genetico": 0.25, "tipo": "ascendente"},
    "avo_materna": {"grau": 2, "compartilhamento_genetico": 0.25, "tipo": "ascendente"},
    "tio": {"grau": 2, "compartilhamento_genetico": 0.25, "tipo": "colateral"},
    "tia": {"grau": 2, "compartilhamento_genetico": 0.25, "tipo": "colateral"},
    "sobrinho": {"grau": 2, "compartilhamento_genetico": 0.25, "tipo": "colateral"},
    "sobrinha": {"grau": 2, "compartilhamento_genetico": 0.25, "tipo": "colateral"},
    "primo": {"grau": 3, "compartilhamento_genetico": 0.125, "tipo": "colateral"},
    "prima": {"grau": 3, "compartilhamento_genetico": 0.125, "tipo": "colateral"},
    "meio_irmao": {"grau": 2, "compartilhamento_genetico": 0.25, "tipo": "meio_irmao"},
    "meia_irma": {"grau": 2, "compartilhamento_genetico": 0.25, "tipo": "meio_irmao"},
}


def calcular_probabilidade_base(doenca_info, parentesco_info, sexo_parente):
    """
    Calcula a probabilidade base de um parente ter a doença
    baseado no tipo de herança e grau de parentesco.
    """
    tipo_heranca = doenca_info["tipo_heranca"]
    penetrancia = doenca_info["penetrancia"]
    compartilhamento = parentesco_info["compartilhamento_genetico"]
    grau = parentesco_info["grau"]

    if tipo_heranca == "autossomica_dominante":
        # 50% chance para parentes de 1o grau, reduz com distância
        if grau == 1:
            prob = 0.50 * penetrancia
        elif grau == 2:
            prob = 0.25 * penetrancia
        else:
            prob = 0.125 * penetrancia

    elif tipo_heranca == "autossomica_recessiva":
        # Ambos pais devem ser portadores
        # Para irmãos: 25% se ambos pais portadores
        if parentesco_info["tipo"] == "irmao":
            prob = 0.25 * penetrancia
        elif parentesco_info["tipo"] == "descendente":
            # Depende se o outro progenitor é portador (assumimos ~4% para doenças comuns)
            prob = 0.02 * penetrancia
        elif parentesco_info["tipo"] == "progenitor":
            prob = 0.01 * penetrancia  # Pais geralmente são portadores, não afetados
        else:
            prob = compartilhamento * 0.10 * penetrancia

    elif tipo_heranca == "ligada_x_recessiva":
        # Homens são mais afetados
        if sexo_parente == "masculino":
            if parentesco_info["tipo"] == "irmao":
                prob = 0.50 * penetrancia  # 50% dos filhos de mãe portadora
            elif parentesco_info["tipo"] == "descendente":
                prob = 0.50 * penetrancia
            else:
                prob = compartilhamento * 0.50 * penetrancia
        else:
            # Mulheres geralmente são portadoras, raramente afetadas
            if parentesco_info["tipo"] == "irmao":
                prob = 0.50 * 0.05  # Portadoras raramente manifestam
            else:
                prob = compartilhamento * 0.05

    elif tipo_heranca == "multifatorial_dominante":
        # Cânceres hereditários - influência genética + ambiental
        if grau == 1:
            prob = 0.50 * penetrancia * 0.85  # Fator ambiental reduz um pouco
        elif grau == 2:
            prob = 0.25 * penetrancia * 0.70
        else:
            prob = 0.125 * penetrancia * 0.55

    else:
        prob = compartilhamento * penetrancia * 0.5

    return min(prob, 0.99)


def gerar_fatores_ambientais():
    """Gera fatores ambientais/estilo de vida aleatórios."""
    return {
        "tabagismo": np.random.choice([0, 1], p=[0.75, 0.25]),
        "alcoolismo": np.random.choice([0, 1], p=[0.85, 0.15]),
        "sedentarismo": np.random.choice([0, 1], p=[0.60, 0.40]),
        "obesidade": np.random.choice([0, 1], p=[0.75, 0.25]),
        "exposicao_quimicos": np.random.choice([0, 1], p=[0.90, 0.10]),
        "dieta_inadequada": np.random.choice([0, 1], p=[0.65, 0.35]),
        "estresse_cronico": np.random.choice([0, 1], p=[0.60, 0.40]),
    }


def ajustar_probabilidade_por_fatores(prob_base, fatores, doenca_info):
    """
    Ajusta a probabilidade base considerando fatores ambientais.
    Fatores ambientais têm mais impacto em doenças multifatoriais.
    """
    if doenca_info["categoria"] == "cancer":
        # Cânceres são mais influenciados por fatores ambientais
        fator_ajuste = 1.0
        if fatores["tabagismo"]:
            fator_ajuste += 0.15
        if fatores["alcoolismo"]:
            fator_ajuste += 0.10
        if fatores["sedentarismo"]:
            fator_ajuste += 0.05
        if fatores["obesidade"]:
            fator_ajuste += 0.10
        if fatores["exposicao_quimicos"]:
            fator_ajuste += 0.20
        if fatores["dieta_inadequada"]:
            fator_ajuste += 0.05
        if fatores["estresse_cronico"]:
            fator_ajuste += 0.03

        prob_ajustada = prob_base * fator_ajuste
    else:
        # Doenças genéticas raras são menos influenciadas por ambiente
        fator_ajuste = 1.0
        if fatores["exposicao_quimicos"]:
            fator_ajuste += 0.05
        if fatores["estresse_cronico"]:
            fator_ajuste += 0.02

        prob_ajustada = prob_base * fator_ajuste

    return min(prob_ajustada, 0.99)


def gerar_dataset(n_amostras=5000):
    """Gera o dataset sintético completo."""
    dados = []

    for _ in range(n_amostras):
        # Selecionar doença aleatória
        doenca_id = np.random.choice(list(DOENCAS.keys()))
        doenca_info = DOENCAS[doenca_id]

        # Selecionar parentesco aleatório
        parentesco_id = np.random.choice(list(PARENTESCOS.keys()))
        parentesco_info = PARENTESCOS[parentesco_id]

        # Determinar sexo do parente
        # Alguns parentescos têm sexo implícito
        parentescos_femininos = ["mae", "filha", "irma", "avo_materna", "tia", "sobrinha", "prima", "meia_irma"]
        parentescos_masculinos = ["pai", "filho", "irmao", "avo_paterno", "tio", "sobrinho", "primo", "meio_irmao"]

        if parentesco_id in parentescos_femininos:
            sexo_parente = "feminino"
        elif parentesco_id in parentescos_masculinos:
            sexo_parente = "masculino"
        else:
            sexo_parente = np.random.choice(["masculino", "feminino"])

        # Idade do parente (afeta expressão de algumas doenças)
        idade_parente = np.random.randint(1, 85)

        # Idade do afetado
        idade_afetado = np.random.randint(1, 85)

        # Número de afetados na família (mais afetados = maior risco)
        num_afetados_familia = np.random.choice([1, 2, 3, 4, 5], p=[0.40, 0.30, 0.15, 0.10, 0.05])

        # Gerar fatores ambientais
        fatores = gerar_fatores_ambientais()

        # Calcular probabilidade base
        prob_base = calcular_probabilidade_base(doenca_info, parentesco_info, sexo_parente)

        # Ajustar por fatores ambientais
        prob_ajustada = ajustar_probabilidade_por_fatores(prob_base, fatores, doenca_info)

        # Ajustar por número de afetados na família
        fator_familia = 1.0 + (num_afetados_familia - 1) * 0.10
        prob_ajustada = min(prob_ajustada * fator_familia, 0.99)

        # Ajustar por idade (algumas doenças são de início tardio)
        if doenca_id in ["huntington", "cancer_mama_brca1", "cancer_mama_brca2",
                         "cancer_prostata", "melanoma_familiar", "sindrome_lynch"]:
            # Doenças de início tardio - risco aumenta com idade
            if idade_parente < 20:
                prob_ajustada *= 0.3
            elif idade_parente < 40:
                prob_ajustada *= 0.7
            elif idade_parente < 60:
                prob_ajustada *= 1.0
            else:
                prob_ajustada *= 1.1
            prob_ajustada = min(prob_ajustada, 0.99)

        # Determinar se o parente desenvolve a doença (variável alvo)
        desenvolve_doenca = 1 if np.random.random() < prob_ajustada else 0

        # Adicionar um pouco de ruído para simular incerteza do mundo real
        prob_com_ruido = prob_ajustada + np.random.normal(0, 0.02)
        prob_com_ruido = max(0.01, min(0.99, prob_com_ruido))

        registro = {
            "doenca_id": doenca_id,
            "doenca_nome": doenca_info["nome"],
            "tipo_heranca": doenca_info["tipo_heranca"],
            "categoria_doenca": doenca_info["categoria"],
            "penetrancia": doenca_info["penetrancia"],
            "parentesco": parentesco_id,
            "grau_parentesco": parentesco_info["grau"],
            "compartilhamento_genetico": parentesco_info["compartilhamento_genetico"],
            "sexo_parente": 1 if sexo_parente == "masculino" else 0,
            "idade_parente": idade_parente,
            "idade_afetado": idade_afetado,
            "num_afetados_familia": num_afetados_familia,
            "tabagismo": fatores["tabagismo"],
            "alcoolismo": fatores["alcoolismo"],
            "sedentarismo": fatores["sedentarismo"],
            "obesidade": fatores["obesidade"],
            "exposicao_quimicos": fatores["exposicao_quimicos"],
            "dieta_inadequada": fatores["dieta_inadequada"],
            "estresse_cronico": fatores["estresse_cronico"],
            "probabilidade_calculada": round(prob_com_ruido, 4),
            "desenvolve_doenca": desenvolve_doenca,
        }
        dados.append(registro)

    df = pd.DataFrame(dados)
    return df


def salvar_metadados():
    """Salva metadados das doenças e parentescos para uso no frontend."""
    metadados = {
        "doencas": DOENCAS,
        "parentescos": {k: {**v, "label": k.replace("_", " ").title()} for k, v in PARENTESCOS.items()},
    }

    output_path = os.path.join(os.path.dirname(__file__), "metadados.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(metadados, f, ensure_ascii=False, indent=2)

    print(f"Metadados salvos em: {output_path}")
    return metadados


if __name__ == "__main__":
    print("Gerando dataset sintético para predição de doenças genéticas...")
    print(f"Doenças disponíveis: {len(DOENCAS)}")
    print(f"Tipos de parentesco: {len(PARENTESCOS)}")

    # Gerar dataset
    df = gerar_dataset(n_amostras=10000)

    # Salvar dataset
    output_path = os.path.join(os.path.dirname(__file__), "dataset_genetico.csv")
    df.to_csv(output_path, index=False)
    print(f"\nDataset salvo em: {output_path}")
    print(f"Total de amostras: {len(df)}")
    print(f"\nDistribuição de doenças:")
    print(df["doenca_nome"].value_counts())
    print(f"\nDistribuição de resultados:")
    print(df["desenvolve_doenca"].value_counts())
    print(f"\nProbabilidade média por grau de parentesco:")
    print(df.groupby("grau_parentesco")["probabilidade_calculada"].mean())

    # Salvar metadados
    salvar_metadados()

    print("\nDataset gerado com sucesso!")
