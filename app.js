/**
 * BookMatch - Sistema de Recomendação de Livros
 * Busca livros na base local e recomenda 5 do mesmo gênero/estilo.
 * Links de compra direcionam para Amazon.com.br
 */

document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('searchInput');
  const searchBtn = document.getElementById('searchBtn');
  const loading = document.getElementById('loading');
  const error = document.getElementById('error');
  const errorMessage = document.getElementById('errorMessage');
  const results = document.getElementById('results');
  const searchedBookEl = document.getElementById('searchedBook');
  const recommendationsEl = document.getElementById('recommendations');

  searchBtn.addEventListener('click', performSearch);
  searchInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') performSearch();
  });

  function performSearch() {
    const title = searchInput.value.trim();
    if (!title) {
      showError('Por favor, digite o nome de um livro.');
      return;
    }

    hideError();
    hideResults();
    showLoading();

    // Simula um pequeno delay para UX
    setTimeout(() => {
      const book = findBook(title);
      if (!book) {
        hideLoading();
        showError('Livro não encontrado na base. Tente: "Harry Potter", "1984", "Dom Casmurro", "O Alquimista"...');
        return;
      }

      const recommendations = getRecommendations(book);
      displayResults(book, recommendations);
      hideLoading();
    }, 600);
  }

  /**
   * Busca um livro pelo título (busca precisa)
   */
  function findBook(query) {
    const q = normalize(query);
    
    // 1. Match exato
    let found = BOOKS_DATABASE.find(b => normalize(b.title) === q);
    if (found) return found;

    // 2. Título contém toda a query ou query contém o título inteiro
    found = BOOKS_DATABASE.find(b => normalize(b.title).includes(q));
    if (found) return found;

    // 3. Todas as palavras da query estão no título
    const words = q.split(/\s+/).filter(w => w.length > 2);
    found = BOOKS_DATABASE.find(b => {
      const titleNorm = normalize(b.title);
      return words.length > 0 && words.every(w => titleNorm.includes(w));
    });
    if (found) return found;

    // 4. A maioria das palavras significativas (>3 letras) da query batem
    const significantWords = q.split(/\s+/).filter(w => w.length > 3);
    if (significantWords.length > 0) {
      let bestMatch = null;
      let bestScore = 0;
      for (const b of BOOKS_DATABASE) {
        const titleNorm = normalize(b.title);
        const matchCount = significantWords.filter(w => titleNorm.includes(w)).length;
        const score = matchCount / significantWords.length;
        if (score > bestScore && score >= 0.6) {
          bestScore = score;
          bestMatch = b;
        }
      }
      if (bestMatch) return bestMatch;
    }

    // 5. Busca por autor
    found = BOOKS_DATABASE.find(b => normalize(b.author).includes(q));
    return found || null;
  }

  /**
   * Retorna 5 recomendações do mesmo gênero/estilo, evitando repetir autor
   */
  function getRecommendations(book) {
    const candidates = BOOKS_DATABASE.filter(b => b.title !== book.title);

    // Pontuar cada candidato por similaridade
    const scored = candidates.map(b => {
      let score = 0;
      
      // Mesmo gênero: +10 pontos
      if (b.genre === book.genre) score += 10;
      
      // Mesmo subgênero: +8 pontos
      if (b.subgenre === book.subgenre) score += 8;
      
      // Época similar (dentro de 30 anos): +2 pontos
      if (Math.abs(b.year - book.year) <= 30) score += 2;
      
      // Rating alto: +1 ponto
      if (b.rating >= 4.3) score += 1;

      // Penalizar mesmo autor: -5 pontos (queremos variedade)
      if (b.author === book.author) score -= 5;

      return { book: b, score };
    });

    // Ordenar por score e pegar os 5 melhores
    scored.sort((a, b) => b.score - a.score);
    
    // Garantir no máximo 1 livro do mesmo autor
    const result = [];
    const authorsUsed = new Set();
    for (const s of scored) {
      if (result.length >= 5) break;
      if (s.book.author === book.author && authorsUsed.has(s.book.author)) continue;
      authorsUsed.add(s.book.author);
      result.push(s.book);
    }
    
    return result;
  }

  function displayResults(book, recommendations) {
    searchedBookEl.innerHTML = renderSearchedBook(book);
    recommendationsEl.innerHTML = recommendations
      .map((rec, i) => renderRecCard(rec, i + 1))
      .join('');
    showResults();
  }

  function renderSearchedBook(book) {
    const coverUrl = book.isbn ? `https://covers.openlibrary.org/b/isbn/${book.isbn}-M.jpg` : '';
    return `
      <div class="book-cover" style="background:${getColorForGenre(book.genre)}">
        ${coverUrl ? `<img src="${coverUrl}" alt="" style="width:100%;height:100%;object-fit:cover;border-radius:6px;" onload="this.style.opacity=1" onerror="this.remove()">` : ''}
        <span class="cover-fallback">${escapeHtml(book.title.substring(0,30))}</span>
      </div>
      <div class="book-info">
        <h3 class="book-title">${escapeHtml(book.title)}</h3>
        <p class="book-author">por ${escapeHtml(book.author)}</p>
        <div class="book-categories">
          <span class="category-tag">${escapeHtml(book.genre)}</span>
          <span class="category-tag">${escapeHtml(book.subgenre)}</span>
        </div>
        <p class="book-description">${escapeHtml(book.description)}</p>
        <div class="book-meta">
          <span>📅 ${book.year}</span>
          <span>📄 ${book.pages} páginas</span>
          <span class="rating">${'★'.repeat(Math.round(book.rating))}${'☆'.repeat(5 - Math.round(book.rating))} ${book.rating}/5</span>
        </div>
        <div class="book-links" style="margin-top: 0.75rem;">
          <a href="${book.amazon}" target="_blank" rel="noopener noreferrer" class="link-amazon">🛒 Ver na Amazon</a>
        </div>
      </div>
    `;
  }

  function renderRecCard(book, index) {
    const colors = ['#6c5ce7','#00b894','#e17055','#0984e3','#e84393','#00cec9','#fd79a8','#636e72'];
    const color = colors[index % colors.length];
    const coverUrl = book.isbn ? `https://covers.openlibrary.org/b/isbn/${book.isbn}-M.jpg` : '';
    return `
      <article class="rec-card">
        <span class="rec-number">${index}</span>
        <div class="book-cover" style="background:${color}">
          ${coverUrl ? `<img src="${coverUrl}" alt="" style="width:100%;height:100%;object-fit:cover;border-radius:6px;" onload="this.style.opacity=1" onerror="this.remove()">` : ''}
          <span class="cover-fallback">${escapeHtml(book.title.substring(0,25))}</span>
        </div>
        <div class="book-info">
          <h3 class="book-title">${escapeHtml(book.title)}</h3>
          <p class="book-author">por ${escapeHtml(book.author)}</p>
          <div class="book-categories">
            <span class="category-tag">${escapeHtml(book.genre)}</span>
            <span class="category-tag">${escapeHtml(book.subgenre)}</span>
          </div>
          <p class="book-description">${escapeHtml(book.description)}</p>
          <div class="rating">${'★'.repeat(Math.round(book.rating))}${'☆'.repeat(5 - Math.round(book.rating))} ${book.rating}/5</div>
          <div class="book-links">
            <a href="${book.amazon}" target="_blank" rel="noopener noreferrer" class="link-amazon">🛒 Amazon</a>
          </div>
        </div>
      </article>
    `;
  }

  // UI Helpers
  function showLoading() { loading.classList.remove('hidden'); }
  function hideLoading() { loading.classList.add('hidden'); }
  function showError(msg) { errorMessage.textContent = msg; error.classList.remove('hidden'); }
  function hideError() { error.classList.add('hidden'); }
  function showResults() { results.classList.remove('hidden'); }
  function hideResults() { results.classList.add('hidden'); }

  function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  function normalize(str) {
    return str.toLowerCase()
      .normalize('NFD').replace(/[\u0300-\u036f]/g, '')
      .replace(/[^a-z0-9\s]/g, '')
      .trim();
  }

  /**
   * Gera uma capa de livro em SVG inline (sem dependência externa)
   */
  function generateCoverSVG(title, author, bgColor) {
    const words = title.split(' ');
    const lines = [];
    let currentLine = '';
    for (const word of words) {
      if ((currentLine + ' ' + word).trim().length > 13) {
        if (currentLine) lines.push(currentLine.trim());
        currentLine = word;
      } else {
        currentLine += ' ' + word;
      }
    }
    if (currentLine.trim()) lines.push(currentLine.trim());

    const titleLines = lines.slice(0, 5);
    const startY = Math.max(35, 80 - (titleLines.length * 10));
    const titleSVG = titleLines.map((line, i) => 
      `<text x="60" y="${startY + i * 17}" text-anchor="middle" fill="white" font-size="10.5" font-weight="bold" font-family="Georgia,serif">${escapeXml(line)}</text>`
    ).join('');

    const authorShort = author.length > 20 ? author.substring(0, 18) + '...' : author;
    const darkerBg = bgColor;

    return `<svg viewBox="0 0 120 180" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:100%;display:block;">
      <defs>
        <linearGradient id="grad${bgColor.replace('#','')}" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" style="stop-color:${darkerBg};stop-opacity:1"/>
          <stop offset="100%" style="stop-color:${darkerBg};stop-opacity:0.7"/>
        </linearGradient>
      </defs>
      <rect width="120" height="180" fill="url(#grad${bgColor.replace('#','')})" rx="3"/>
      <rect x="5" y="5" width="110" height="170" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="0.8" rx="2"/>
      <rect x="10" y="20" width="100" height="2" fill="rgba(255,255,255,0.3)"/>
      ${titleSVG}
      <rect x="10" y="${startY + titleLines.length * 17 + 5}" width="100" height="1" fill="rgba(255,255,255,0.2)"/>
      <text x="60" y="160" text-anchor="middle" fill="rgba(255,255,255,0.7)" font-size="8.5" font-family="Arial,sans-serif">${escapeXml(authorShort)}</text>
    </svg>`;
  }

  function escapeXml(text) {
    return text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  function getColorForGenre(genre) {
    const colors = {
      'Suspense': '#e17055',
      'Terror': '#2d3436',
      'Romance': '#e84393',
      'Fantasia': '#6c5ce7',
      'Ficção Científica': '#0984e3',
      'Aventura': '#00b894',
      'Autoajuda': '#fdcb6e',
      'Biografia': '#00cec9',
      'Literatura Brasileira': '#55a630',
      'Infantil': '#fd79a8'
    };
    return colors[genre] || '#636e72';
  }
});
