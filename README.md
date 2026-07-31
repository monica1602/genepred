# GenePred - Sistema de Predicao de Doencas Geneticas com Machine Learning

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-green?logo=flask)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3%2B-orange?logo=scikit-learn)
![License](https://img.shields.io/badge/License-MIT-yellow)

Sistema web que utiliza Machine Learning para estimar a probabilidade de um parente desenvolver uma doenca genetica, com base nos dados de um familiar ja diagnosticado.

## Acesse o Site

**[genepred.onrender.com](https://genepred.onrender.com)**

---

> **Aviso:** Este sistema e uma ferramenta educacional e de estimativa. Nao substitui aconselhamento genetico profissional nem diagnostico medico.

---

## Visao Geral

O GenePred analisa padroes de heranca genetica, grau de parentesco, penetrancia da doenca e fatores ambientais para calcular uma estimativa de risco. O modelo utiliza um ensemble de **Random Forest** (classificacao) e **Gradient Boosting** (regressao de probabilidade).

### Funcionalidades

- Predicao de risco para **76 doencas geneticas** divididas em 7 categorias
- Calculo baseado em padroes reais de heranca mendeliana
- Consideracao de **fatores ambientais e estilo de vida**
- Interface web responsiva com visualizacao grafica dos resultados
- Geracao de recomendacoes personalizadas por nivel de risco
- API REST para integracao com outros sistemas

---

## Doencas Cobertas

| Categoria | Qtd | Exemplos |
|-----------|:---:|---------|
| Canceres Hereditarios | 18 | Mama (BRCA1/2), Li-Fraumeni, Lynch, Pancreas, Pulmao |
| Doencas Autoimunes | 15 | Lupus, Artrite Reumatoide, Esclerose Multipla, Crohn, Celiaca |
| Doencas Geneticas Raras | 20 | Huntington, Marfan, Fibrose Cistica, Tay-Sachs, Gaucher |
| Cardiovasculares | 7 | Cardiomiopatia Hipertrofica, QT Longo, Brugada |
| Neurologicas | 6 | Alzheimer Familiar, Parkinson, ELA, Charcot-Marie-Tooth |
| Metabolicas | 6 | Diabetes MODY, Hemocromatose, Galactosemia |
| Psiquiatricas | 4 | Esquizofrenia, Bipolar, TEA, TDAH |

---

## Tipos de Heranca Suportados

- **Autossomica Dominante** - 50% de chance para filhos de afetados (ex: Huntington)
- **Autossomica Recessiva** - Requer duas copias do gene alterado (ex: Fibrose Cistica)
- **Ligada ao X Recessiva** - Homens mais afetados (ex: Hemofilia, Duchenne)
- **Multifatorial Dominante** - Gene dominante + influencia ambiental (ex: BRCA1/2)
- **Multifatorial Poligenica** - Multiplos genes + ambiente (ex: Lupus, Diabetes Tipo 1)

---

## Arquitetura

```
genepred/
├── backend/
│   ├── app.py                      # API Flask + treinamento sem pandas
│   ├── data/
│   │   └── generate_dataset.py     # Gerador de dataset sintetico
│   └── models/
│       ├── genetic_predictor.py    # Modelo ML (RF + GBR)
│       └── trained_model.pkl       # Modelo pre-treinado
├── frontend/
│   ├── index.html                  # Interface principal
│   └── static/
│       ├── styles.css              # Estilos
│       └── app.js                  # Logica do frontend
├── requirements.txt                # Dependencias Python
├── render.yaml                     # Configuracao de deploy (Render)
├── Procfile                        # Configuracao de processo
└── run.py                          # Script para execucao local
```

---

## Como Executar Localmente

### Pre-requisitos

- Python 3.10 ou superior

### Instalacao

```bash
# Clonar o repositorio
git clone https://github.com/monica1602/genepred.git
cd genepred

# Instalar dependencias
pip install -r requirements.txt

# Para treinamento local com dataset completo (opcional)
pip install pandas
```

### Execucao

```bash
python run.py
```

Acesse **http://localhost:5000** no navegador.

Na primeira execucao, o modelo sera treinado automaticamente (~10 segundos).

---

## API REST

### POST /api/predict

Faz a predicao de risco genetico.

**Request:**
```json
{
  "doenca_id": "cancer_mama_brca1",
  "parentesco": "irma",
  "sexo_parente": 0,
  "idade_parente": 40,
  "idade_afetado": 55,
  "num_afetados_familia": 2,
  "tabagismo": 0,
  "alcoolismo": 0,
  "sedentarismo": 1,
  "obesidade": 0,
  "exposicao_quimicos": 0,
  "dieta_inadequada": 0,
  "estresse_cronico": 1
}
```

**Response:**
```json
{
  "probabilidade": 42.88,
  "nivel_risco": "Moderado",
  "cor_risco": "#ffc107",
  "confianca_modelo": 54.4,
  "recomendacoes": ["..."],
  "doenca_info": { "nome": "Cancer de Mama (BRCA1)", "tipo_heranca": "..." },
  "parentesco_info": { "parentesco": "irma", "grau": 1 }
}
```

### GET /api/diseases

Lista todas as doencas disponiveis.

### GET /api/relationships

Lista todos os graus de parentesco disponiveis.

### GET /api/model-info

Retorna metricas e informacoes do modelo treinado.

---

## Modelo de Machine Learning

### Algoritmos

| Componente | Algoritmo | Funcao |
|-----------|-----------|--------|
| Classificador | Random Forest | Classifica se ha risco ou nao |
| Regressor | Gradient Boosting | Estima a probabilidade percentual |
| Resultado Final | Ensemble (40% RF + 60% GBR) | Combinacao ponderada |

### Features Utilizadas

**Geneticas:**
- Grau de parentesco e compartilhamento genetico (%)
- Tipo de heranca da doenca
- Penetrancia da doenca
- Numero de afetados na familia

**Demograficas:**
- Sexo e idade do parente avaliado
- Idade do parente afetado

**Ambientais:**
- Tabagismo, alcoolismo, sedentarismo
- Obesidade, exposicao a quimicos
- Dieta inadequada, estresse cronico

### Metricas (validacao cruzada)

- **ROC-AUC:** ~0.78
- **Acuracia:** ~80%
- **MAE (regressao):** ~0.03

---

## Base de Dados

O dataset e **sintetico**, gerado com parametros baseados na literatura medica:

**Baseado em ciencia real:**
- Padroes de heranca mendeliana
- Penetrancias publicadas (ex: BRCA1 ~72%, Huntington ~95%)
- Compartilhamento genetico real por grau de parentesco
- Influencia de fatores ambientais segundo evidencias epidemiologicas

**Limitacoes:**
- Nao utiliza dados reais de pacientes
- Simplifica interacoes gene-gene e epigenetica
- Nao considera variantes geneticas especificas

---

## Deploy

O projeto esta configurado para deploy no [Render](https://render.com):

1. Conecte o repositorio no Render
2. Configure como **Web Service** com Python
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn --chdir backend app:app --bind 0.0.0.0:$PORT`
5. Adicione variavel de ambiente: `PYTHON_VERSION=3.11.9`

---

## Tecnologias

- **Backend:** Python, Flask, scikit-learn, NumPy
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **ML:** Random Forest, Gradient Boosting, Feature Engineering
- **Deploy:** Gunicorn, Render

---

## Licenca

Este projeto esta sob a licenca MIT.

---

## Disclaimer

Este sistema e uma ferramenta **educacional** desenvolvida para fins de estudo e demonstracao de Machine Learning aplicado a genetica. **Nao possui finalidade diagnostica.** Para avaliacao de risco genetico real, consulte um geneticista clinico e realize testes geneticos especificos.
