# GenePred - Sistema de Predição de Doenças Genéticas com Machine Learning

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-green?logo=flask)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3%2B-orange?logo=scikit-learn)
![License](https://img.shields.io/badge/License-MIT-yellow)

Sistema web que utiliza Machine Learning para estimar a probabilidade de um parente desenvolver uma doença genética, com base nos dados de um familiar já diagnosticado.

> **Aviso:** Este sistema é uma ferramenta educacional e de estimativa. Não substitui aconselhamento genético profissional nem diagnóstico médico.

---

## Visão Geral

O GenePred analisa padrões de herança genética, grau de parentesco, penetrância da doença e fatores ambientais para calcular uma estimativa de risco. O modelo utiliza um ensemble de **Random Forest** (classificação) e **Gradient Boosting** (regressão de probabilidade).

### Funcionalidades

- Predição de risco para **76 doenças genéticas** divididas em 7 categorias
- Cálculo baseado em padrões reais de herança mendeliana
- Consideração de **fatores ambientais e estilo de vida**
- Interface web responsiva com visualização gráfica dos resultados
- Geração de recomendações personalizadas por nível de risco
- API REST para integração com outros sistemas

---

## Doenças Cobertas

| Categoria | Qtd | Exemplos |
|-----------|:---:|---------|
| Cânceres Hereditários | 18 | Mama (BRCA1/2), Li-Fraumeni, Lynch, Pâncreas, Pulmão |
| Doenças Autoimunes | 15 | Lúpus, Artrite Reumatoide, Esclerose Múltipla, Crohn, Celíaca |
| Doenças Genéticas Raras | 20 | Huntington, Marfan, Fibrose Cística, Tay-Sachs, Gaucher |
| Cardiovasculares | 7 | Cardiomiopatia Hipertrófica, QT Longo, Brugada |
| Neurológicas | 6 | Alzheimer Familiar, Parkinson, ELA, Charcot-Marie-Tooth |
| Metabólicas | 6 | Diabetes MODY, Hemocromatose, Galactosemia |
| Psiquiátricas | 4 | Esquizofrenia, Bipolar, TEA, TDAH |

---

## Tipos de Herança Suportados

- **Autossômica Dominante** — 50% de chance para filhos de afetados (ex: Huntington)
- **Autossômica Recessiva** — Requer duas cópias do gene alterado (ex: Fibrose Cística)
- **Ligada ao X Recessiva** — Homens mais afetados (ex: Hemofilia, Duchenne)
- **Multifatorial Dominante** — Gene dominante + influência ambiental (ex: BRCA1/2)
- **Multifatorial Poligênica** — Múltiplos genes + ambiente (ex: Lúpus, Diabetes Tipo 1)

---

## Arquitetura

```
genepred/
├── backend/
│   ├── app.py                      # API Flask + treinamento sem pandas
│   ├── data/
│   │   └── generate_dataset.py     # Gerador de dataset sintético
│   └── models/
│       ├── genetic_predictor.py    # Modelo ML (RF + GBR)
│       └── trained_model.pkl       # Modelo pré-treinado
├── frontend/
│   ├── index.html                  # Interface principal
│   └── static/
│       ├── styles.css              # Estilos
│       └── app.js                  # Lógica do frontend
├── requirements.txt                # Dependências Python
├── render.yaml                     # Configuração de deploy (Render)
├── Procfile                        # Configuração de processo
└── run.py                          # Script para execução local
```

---

## Como Executar Localmente

### Pré-requisitos

- Python 3.10 ou superior

### Instalação

```bash
# Clonar o repositório
git clone https://github.com/monica1602/genepred.git
cd genepred

# Instalar dependências
pip install -r requirements.txt

# Para treinamento local com dataset completo (opcional)
pip install pandas
```

### Execução

```bash
python run.py
```

Acesse **http://localhost:5000** no navegador.

Na primeira execução, o modelo será treinado automaticamente (~10 segundos).

---

## API REST

### POST /api/predict

Faz a predição de risco genético.

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
  "doenca_info": { "nome": "Câncer de Mama (BRCA1)", "tipo_heranca": "..." },
  "parentesco_info": { "parentesco": "irma", "grau": 1 }
}
```

### GET /api/diseases

Lista todas as doenças disponíveis.

### GET /api/relationships

Lista todos os graus de parentesco disponíveis.

### GET /api/model-info

Retorna métricas e informações do modelo treinado.

---

## Modelo de Machine Learning

### Algoritmos

| Componente | Algoritmo | Função |
|-----------|-----------|--------|
| Classificador | Random Forest | Classifica se há risco ou não |
| Regressor | Gradient Boosting | Estima a probabilidade percentual |
| Resultado Final | Ensemble (40% RF + 60% GBR) | Combinação ponderada |

### Features Utilizadas

**Genéticas:**
- Grau de parentesco e compartilhamento genético (%)
- Tipo de herança da doença
- Penetrância da doença
- Número de afetados na família

**Demográficas:**
- Sexo e idade do parente avaliado
- Idade do parente afetado

**Ambientais:**
- Tabagismo, alcoolismo, sedentarismo
- Obesidade, exposição a químicos
- Dieta inadequada, estresse crônico

### Métricas (validação cruzada)

- **ROC-AUC:** ~0.78
- **Acurácia:** ~80%
- **MAE (regressão):** ~0.03

---

## Base de Dados

O dataset é **sintético**, gerado com parâmetros baseados na literatura médica:

**Baseado em ciência real:**
- Padrões de herança mendeliana
- Penetrâncias publicadas (ex: BRCA1 ~72%, Huntington ~95%)
- Compartilhamento genético real por grau de parentesco
- Influência de fatores ambientais segundo evidências epidemiológicas

**Limitações:**
- Não utiliza dados reais de pacientes
- Simplifica interações gene-gene e epigenética
- Não considera variantes genéticas específicas

---

## Deploy

O projeto está configurado para deploy no [Render](https://render.com):

1. Conecte o repositório no Render
2. Configure como **Web Service** com Python
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn --chdir backend app:app --bind 0.0.0.0:$PORT`
5. Adicione variável de ambiente: `PYTHON_VERSION=3.11.9`

---

## Tecnologias

- **Backend:** Python, Flask, scikit-learn, NumPy
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **ML:** Random Forest, Gradient Boosting, Feature Engineering
- **Deploy:** Gunicorn, Render

---

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## Disclaimer

Este sistema é uma ferramenta **educacional** desenvolvida para fins de estudo e demonstração de Machine Learning aplicado à genética. **Não possui finalidade diagnóstica.** Para avaliação de risco genético real, consulte um geneticista clínico e realize testes genéticos específicos.
