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
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

# Adicionar diretórios ao path
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'models'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'data'))

from models.genetic_predictor import GeneticDiseasePredictor, train_and_save
from data.generate_dataset import DOENCAS, PARENTESCOS

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
            print(f"Erro ao carregar modelo: {e}. Retreinando...")
            predictor = train_and_save()
    else:
        print("Modelo não encontrado. Treinando novo modelo...")
        predictor = train_and_save()

    return predictor


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


if __name__ == '__main__':
    print("Inicializando Sistema de Predição de Doenças Genéticas...")
    print("Carregando modelo...")

    # Pré-carregar modelo
    get_predictor()

    print("\nServidor iniciado!")
    print("Acesse: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
