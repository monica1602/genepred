# 📚 BookMatch - Recomendação de Livros

Sistema inteligente de recomendação de livros. Digite o nome de um livro e receba **5 sugestões** do mesmo gênero e estilo de escrita, com links diretos para compra na Amazon.

## 🌐 Acesse o Site

**[bookmatch.onrender.com](https://bookmatch.onrender.com)** (ou o link do seu deploy)

---

## 🎯 Como Funciona

1. O usuário digita o nome de um livro que gostou
2. O sistema identifica o gênero, subgênero e estilo
3. Retorna **5 livros recomendados** de outros autores com estilo similar
4. Cada resultado inclui capa, descrição, avaliação e link para Amazon.com.br

---

## 📖 Base de Dados

O site conta com uma base local de **+1800 livros** organizados por gênero:

| Gênero | Exemplos |
|--------|----------|
| Suspense / Thriller | Harlan Coben, Agatha Christie, Freida McFadden, Gillian Flynn |
| Terror | Stephen King, H.P. Lovecraft, Anne Rice, Dean Koontz |
| Romance | Colleen Hoover, Nicholas Sparks, Julia Quinn, Jane Austen |
| Fantasia | Tolkien, Sarah J. Maas, Brandon Sanderson, Leigh Bardugo |
| Ficção Científica | Isaac Asimov, Frank Herbert, George Orwell, Liu Cixin |
| Juvenil / YA | John Green, Thalita Rebouças, Paula Pimenta, Rick Riordan |
| Infantil | Monteiro Lobato, Ziraldo, Roald Dahl, Ruth Rocha |
| Literatura Brasileira | Machado de Assis, Clarice Lispector, Jorge Amado |
| Biografias | Atletas, músicos, líderes mundiais, artistas |
| Autoajuda | Produtividade, finanças, psicologia, filosofia |
| Fatos Reais | Holocausto, crimes, guerras, sobrevivência |
| Romance de Época | Diana Gabaldon, Lisa Kleypas, Ken Follett |
| Dark Romance | Ana Huang, Penelope Douglas, H.D. Carlton |
| Mangás | Death Note, Naruto, One Piece, Demon Slayer |
| Culinária | Rita Lobo, Jamie Oliver, Anthony Bourdain |
| Ciência | Carl Sagan, Stephen Hawking, Yuval Harari |
| História | Laurentino Gomes, Antony Beevor |
| Filosofia | Platão, Nietzsche, Sêneca, Camus |

---

## 🛠️ Tecnologias

- **HTML5** - Estrutura semântica e acessível
- **CSS3** - Design responsivo com variáveis CSS e grid layout
- **JavaScript** - Lógica de busca fuzzy e sistema de pontuação por similaridade
- **Open Library Covers API** - Capas dos livros via ISBN
- **Amazon.com.br** - Links de compra para cada livro

---

## 🚀 Como Rodar Localmente

```bash
# Clone o repositório
git clone https://github.com/monica1602/bookmatch.git

# Entre na pasta
cd bookmatch

# Inicie um servidor local
python -m http.server 8080

# Acesse no navegador
# http://localhost:8080
```

> Não precisa de npm install nem dependências externas.

---

## 🔍 Algoritmo de Recomendação

O sistema usa um algoritmo de pontuação baseado em:

| Critério | Pontos |
|----------|--------|
| Mesmo gênero | +10 |
| Mesmo subgênero | +8 |
| Época similar (30 anos) | +2 |
| Rating alto (4.3+) | +1 |
| Mesmo autor | -5 (penalidade para variedade) |

Além disso, o sistema garante **no máximo 1 livro do mesmo autor** nas recomendações, priorizando diversidade.

---

## 📱 Responsivo

O site funciona em:
- Desktop
- Tablet
- Celular

---

## 📂 Estrutura do Projeto

```
bookmatch/
├── index.html        # Página principal
├── styles.css        # Estilos responsivos
├── app.js            # Lógica de busca e recomendação
├── books-data.js     # Base de dados com +1800 livros
└── README.md         # Este arquivo
```

---

## 🤝 Contribuições

Quer adicionar mais livros ou melhorar o algoritmo? Fique à vontade para abrir um Pull Request!

---

## 📄 Licença

Este projeto é de uso livre para fins educacionais e pessoais.

---

Feito com 💜 usando Kiro AI
