"""
Script principal para executar o GenePred.
Execute este arquivo para iniciar o sistema.
"""

import sys
import os

# Adicionar diretório raiz ao path
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from backend.app import app, get_predictor

if __name__ == '__main__':
    print("=" * 60)
    print("  GenePred - Sistema de Predição de Doenças Genéticas")
    print("=" * 60)
    print()
    print("Inicializando modelo de Machine Learning...")
    print("(Isso pode levar alguns segundos na primeira execução)")
    print()

    # Pré-carregar modelo
    get_predictor()

    print()
    print("Servidor iniciado com sucesso!")
    print("Acesse: http://localhost:5000")
    print()
    print("Pressione Ctrl+C para encerrar")
    print("=" * 60)

    app.run(debug=False, host='0.0.0.0', port=5000)
