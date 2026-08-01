/**
 * GenePred - Frontend Application
 * Sistema de Predição de Doenças Genéticas com Machine Learning
 */

const API_BASE = window.location.origin;

// ============================================
// Inicialização
// ============================================

document.addEventListener('DOMContentLoaded', () => {
    loadDiseases();
    loadRelationships();
    setupFormHandlers();
});

// ============================================
// Carregar dados do backend
// ============================================

async function loadDiseases() {
    try {
        const response = await fetch(`${API_BASE}/api/diseases`);
        const diseases = await response.json();

        const select = document.getElementById('doenca_id');

        // Agrupar por categoria
        const categories = {
            'cancer': { label: 'Cânceres Hereditários', items: [] },
            'autoimune': { label: 'Doenças Autoimunes', items: [] },
            'doenca_rara': { label: 'Doenças Genéticas Raras', items: [] },
            'cardiovascular': { label: 'Doenças Cardiovasculares Hereditárias', items: [] },
            'neurologica': { label: 'Doenças Neurológicas', items: [] },
            'metabolica': { label: 'Doenças Metabólicas', items: [] },
            'psiquiatrica': { label: 'Doenças Psiquiátricas (Componente Genético)', items: [] },
        };

        diseases.forEach(d => {
            if (categories[d.categoria]) {
                categories[d.categoria].items.push(d);
            }
        });

        // Criar optgroups para cada categoria
        Object.values(categories).forEach(cat => {
            if (cat.items.length === 0) return;
            const optgroup = document.createElement('optgroup');
            optgroup.label = cat.label;
            cat.items.forEach(d => {
                const option = document.createElement('option');
                option.value = d.id;
                option.textContent = d.nome;
                option.dataset.category = d.categoria;
                option.dataset.inheritance = d.tipo_heranca;
                option.dataset.penetrance = d.penetrancia;
                optgroup.appendChild(option);
            });
            select.appendChild(optgroup);
        });

        // Event listener para mostrar info da doença
        select.addEventListener('change', showDiseaseInfo);
        select.addEventListener('change', loadSymptomsForDisease);

    } catch (error) {
        console.error('Erro ao carregar doenças:', error);
    }
}

async function loadRelationships() {
    try {
        const response = await fetch(`${API_BASE}/api/relationships`);
        const relationships = await response.json();

        const select = document.getElementById('parentesco');

        // Agrupar por grau
        const grau1 = relationships.filter(r => r.grau === 1);
        const grau2 = relationships.filter(r => r.grau === 2);
        const grau3 = relationships.filter(r => r.grau === 3);

        const groups = [
            { label: '1º Grau (50% DNA compartilhado)', items: grau1 },
            { label: '2º Grau (25% DNA compartilhado)', items: grau2 },
            { label: '3º Grau (12.5% DNA compartilhado)', items: grau3 },
        ];

        groups.forEach(group => {
            if (group.items.length === 0) return;
            const optgroup = document.createElement('optgroup');
            optgroup.label = group.label;
            group.items.forEach(r => {
                const option = document.createElement('option');
                option.value = r.id;
                option.textContent = r.label;
                option.dataset.degree = r.grau;
                option.dataset.sharing = r.compartilhamento_genetico;
                optgroup.appendChild(option);
            });
            select.appendChild(optgroup);
        });

        // Event listener para mostrar info do parentesco
        select.addEventListener('change', showRelationshipInfo);

    } catch (error) {
        console.error('Erro ao carregar parentescos:', error);
    }
}

// ============================================
// Info boxes
// ============================================

function showDiseaseInfo() {
    const select = document.getElementById('doenca_id');
    const selectedOption = select.options[select.selectedIndex];
    const infoBox = document.getElementById('disease-info-box');

    if (!selectedOption.value) {
        infoBox.style.display = 'none';
        return;
    }

    const category = selectedOption.dataset.category;
    const inheritance = selectedOption.dataset.inheritance;
    const penetrance = selectedOption.dataset.penetrance;

    const categoryLabels = {
        'cancer': 'Câncer Hereditário',
        'doenca_rara': 'Doença Rara',
        'autoimune': 'Doença Autoimune',
        'cardiovascular': 'Cardiovascular',
        'neurologica': 'Neurológica',
        'metabolica': 'Metabólica',
        'psiquiatrica': 'Psiquiátrica'
    };

    const inheritanceLabels = {
        'autossomica_dominante': 'Autossômica Dominante',
        'autossomica_recessiva': 'Autossômica Recessiva',
        'ligada_x_recessiva': 'Ligada ao X Recessiva',
        'multifatorial_dominante': 'Multifatorial Dominante',
        'multifatorial_poligenica': 'Multifatorial Poligênica'
    };

    document.getElementById('disease-category').textContent = categoryLabels[category] || category;
    document.getElementById('disease-inheritance').textContent = inheritanceLabels[inheritance] || inheritance;
    document.getElementById('disease-penetrance').textContent = `Penetrância: ${(penetrance * 100).toFixed(0)}%`;

    infoBox.style.display = 'flex';
}

// ============================================
// Sintomas Dinâmicos
// ============================================

let currentSymptoms = [];

async function loadSymptomsForDisease() {
    const select = document.getElementById('doenca_id');
    const doencaId = select.value;
    const fieldset = document.getElementById('symptoms-fieldset');
    const grid = document.getElementById('symptoms-grid');
    const loadingEl = document.getElementById('symptoms-loading');
    const noSymptomsMsg = document.getElementById('no-symptoms-msg');
    const counter = document.getElementById('symptoms-counter');

    // Limpar seleção anterior
    currentSymptoms = [];
    grid.innerHTML = '';
    counter.style.display = 'none';
    document.getElementById('symptoms-count').textContent = '0';

    if (!doencaId) {
        fieldset.style.display = 'none';
        return;
    }

    fieldset.style.display = 'block';
    loadingEl.style.display = 'flex';
    noSymptomsMsg.style.display = 'none';

    try {
        const response = await fetch(`${API_BASE}/api/symptoms/${doencaId}`);
        const data = await response.json();
        const sintomas = data.sintomas || [];

        loadingEl.style.display = 'none';

        if (sintomas.length === 0) {
            noSymptomsMsg.style.display = 'flex';
            return;
        }

        counter.style.display = 'flex';
        sintomas.forEach(sintoma => {
            const label = document.createElement('label');
            label.className = 'checkbox-item symptom-item';
            label.innerHTML = `
                <input type="checkbox" class="symptom-check" value="${sintoma.id}" data-peso="${sintoma.peso}">
                <span class="checkmark"></span>
                <span class="checkbox-label">
                    <i class="fas ${sintoma.icone}"></i> ${sintoma.label}
                </span>
            `;
            grid.appendChild(label);
        });

        // Atualizar contador ao marcar/desmarcar
        grid.querySelectorAll('.symptom-check').forEach(cb => {
            cb.addEventListener('change', () => {
                const checked = grid.querySelectorAll('.symptom-check:checked').length;
                document.getElementById('symptoms-count').textContent = checked;
            });
        });

    } catch (error) {
        loadingEl.style.display = 'none';
        noSymptomsMsg.style.display = 'flex';
        console.error('Erro ao carregar sintomas:', error);
    }
}

function getSelectedSymptoms() {
    const checks = document.querySelectorAll('.symptom-check:checked');
    return Array.from(checks).map(cb => cb.value);
}

function showRelationshipInfo() {
    const select = document.getElementById('parentesco');
    const selectedOption = select.options[select.selectedIndex];
    const infoBox = document.getElementById('relationship-info-box');

    if (!selectedOption.value) {
        infoBox.style.display = 'none';
        return;
    }

    const degree = selectedOption.dataset.degree;
    const sharing = selectedOption.dataset.sharing;

    document.getElementById('rel-degree').textContent = `${degree}º Grau`;
    document.getElementById('rel-sharing').textContent = `${(sharing * 100).toFixed(1)}% DNA compartilhado`;

    infoBox.style.display = 'flex';
}

// ============================================
// Form Handlers
// ============================================

function setupFormHandlers() {
    const form = document.getElementById('prediction-form');
    const resetBtn = document.getElementById('btn-reset');

    form.addEventListener('submit', handleSubmit);

    resetBtn.addEventListener('click', () => {
        document.getElementById('results-section').style.display = 'none';
        document.getElementById('disease-info-box').style.display = 'none';
        document.getElementById('relationship-info-box').style.display = 'none';
        document.getElementById('symptoms-fieldset').style.display = 'none';
        document.getElementById('symptoms-grid').innerHTML = '';
        document.getElementById('symptoms-count').textContent = '0';
    });
}

async function handleSubmit(event) {
    event.preventDefault();

    const form = event.target;
    const submitBtn = document.getElementById('btn-submit');
    const loading = document.getElementById('loading');
    const resultsSection = document.getElementById('results-section');

    // Validar formulário
    if (!form.checkValidity()) {
        form.reportValidity();
        return;
    }

    // Mostrar loading
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processando...';
    loading.style.display = 'block';
    resultsSection.style.display = 'none';

    // Coletar dados
    const data = {
        doenca_id: document.getElementById('doenca_id').value,
        parentesco: document.getElementById('parentesco').value,
        sexo_parente: parseInt(document.getElementById('sexo_parente').value),
        idade_parente: parseInt(document.getElementById('idade_parente').value),
        idade_afetado: parseInt(document.getElementById('idade_afetado').value),
        num_afetados_familia: parseInt(document.getElementById('num_afetados_familia').value),
        tabagismo: document.getElementById('tabagismo').checked ? 1 : 0,
        alcoolismo: document.getElementById('alcoolismo').checked ? 1 : 0,
        sedentarismo: document.getElementById('sedentarismo').checked ? 1 : 0,
        obesidade: document.getElementById('obesidade').checked ? 1 : 0,
        exposicao_quimicos: document.getElementById('exposicao_quimicos').checked ? 1 : 0,
        dieta_inadequada: document.getElementById('dieta_inadequada').checked ? 1 : 0,
        estresse_cronico: document.getElementById('estresse_cronico').checked ? 1 : 0,
        sintomas: getSelectedSymptoms(),
    };

    try {
        const response = await fetch(`${API_BASE}/api/predict`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Erro na predição');
        }

        const result = await response.json();
        displayResults(result);

    } catch (error) {
        alert(`Erro: ${error.message}\n\nVerifique se o servidor backend está rodando.`);
        console.error('Erro na predição:', error);
    } finally {
        submitBtn.disabled = false;
        submitBtn.innerHTML = '<i class="fas fa-calculator"></i> Calcular Probabilidade';
        loading.style.display = 'none';
    }
}

// ============================================
// Display Results
// ============================================

function displayResults(result) {
    const resultsSection = document.getElementById('results-section');

    // Animar o círculo de probabilidade
    const probability = result.probabilidade;
    const circumference = 2 * Math.PI * 54; // r=54
    const offset = circumference - (probability / 100) * circumference;

    const progressCircle = document.getElementById('progress-circle');
    progressCircle.style.stroke = result.cor_risco;
    progressCircle.style.strokeDashoffset = circumference;

    // Mostrar número com animação
    const probNumber = document.getElementById('probability-number');
    probNumber.textContent = '0';

    // Risk badge
    const riskBadge = document.getElementById('risk-badge');
    riskBadge.style.backgroundColor = result.cor_risco + '20';
    riskBadge.style.color = result.cor_risco;
    riskBadge.style.border = `2px solid ${result.cor_risco}`;
    document.getElementById('risk-level').textContent = `Risco ${result.nivel_risco}`;

    // Info grid
    document.getElementById('result-disease').textContent = result.doenca_info.nome;
    document.getElementById('result-relationship').textContent =
        result.parentesco_info.parentesco.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase());

    const inheritanceLabels = {
        'autossomica_dominante': 'Autossômica Dominante',
        'autossomica_recessiva': 'Autossômica Recessiva',
        'ligada_x_recessiva': 'Ligada ao X Recessiva',
        'multifatorial_dominante': 'Multifatorial Dominante',
        'multifatorial_poligenica': 'Multifatorial Poligênica'
    };
    document.getElementById('result-inheritance').textContent =
        inheritanceLabels[result.doenca_info.tipo_heranca] || result.doenca_info.tipo_heranca;
    document.getElementById('result-confidence').textContent = `${result.confianca_modelo}%`;

    // Technical details
    document.getElementById('tech-classifier').textContent = `${result.prob_classificador}%`;
    document.getElementById('tech-regressor').textContent = `${result.prob_regressor}%`;
    document.getElementById('tech-sharing').textContent =
        `${(result.parentesco_info.compartilhamento_genetico * 100).toFixed(1)}%`;
    document.getElementById('tech-penetrance').textContent =
        `${(result.doenca_info.penetrancia * 100).toFixed(0)}%`;

    // Recommendations
    const recList = document.getElementById('recommendations-list');
    recList.innerHTML = '';
    result.recomendacoes.forEach(rec => {
        const li = document.createElement('li');
        li.textContent = rec;
        recList.appendChild(li);
    });

    // ── Sintomas Relatados no resultado ───────────────────────────

    const symptomsResult = document.getElementById('symptoms-result');
    const symptomsResultGrid = document.getElementById('symptoms-result-grid');
    const sintomosRelatados = result.sintomas_relatados || [];
    const sintomasDisponiveis = result.sintomas_disponiveis || [];

    symptomsResultGrid.innerHTML = '';

    if (sintomosRelatados.length > 0) {
        // Montar mapa id -> label
        const mapaLabels = {};
        sintomasDisponiveis.forEach(s => { mapaLabels[s.id] = { label: s.label, icone: s.icone }; });

        sintomosRelatados.forEach(id => {
            const info = mapaLabels[id] || { label: id, icone: 'fa-circle-dot' };
            const chip = document.createElement('div');
            chip.className = 'symptom-result-chip';
            chip.innerHTML = `<i class="fas ${info.icone}"></i><span>${info.label}</span>`;
            symptomsResultGrid.appendChild(chip);
        });
        symptomsResult.style.display = 'block';
    } else {
        symptomsResult.style.display = 'none';
    }

    // ── Clinical Info ──────────────────────────────────────────────

    const ci = result.clinical_info || {};

    // Urgency card
    const urgencyCard = document.getElementById('urgency-card');
    const urgency = ci.urgencia || 'eletiva';
    urgencyCard.className = `urgency-card urgency-${urgency}`;

    const urgencyIcon = document.getElementById('urgency-icon');
    urgencyIcon.className = `fas ${ci.urgencia_icone || 'fa-calendar-check'}`;

    document.getElementById('urgency-tag').textContent = urgency.charAt(0).toUpperCase() + urgency.slice(1);
    document.getElementById('urgency-label').textContent = ci.urgencia_label || '';
    document.getElementById('urgency-description').textContent = ci.urgencia_descricao || '';

    const urgencyIconWrap = document.getElementById('urgency-icon-wrap');
    urgencyIconWrap.style.backgroundColor = (ci.urgencia_cor || '#28a745') + '20';
    urgencyIconWrap.style.color = ci.urgencia_cor || '#28a745';
    document.getElementById('urgency-tag').style.backgroundColor = (ci.urgencia_cor || '#28a745') + '20';
    document.getElementById('urgency-tag').style.color = ci.urgencia_cor || '#28a745';
    document.getElementById('urgency-tag').style.borderColor = ci.urgencia_cor || '#28a745';
    document.getElementById('urgency-label').style.color = ci.urgencia_cor || '#28a745';

    // Specialists
    const specialistsGrid = document.getElementById('specialists-grid');
    specialistsGrid.innerHTML = '';
    const specialistIcons = {
        'Cardiologista': 'fa-heart',
        'Neurologista': 'fa-brain',
        'Oncologista': 'fa-ribbon',
        'Geneticista': 'fa-dna',
        'Hematologista': 'fa-tint',
        'Reumatologista': 'fa-bone',
        'Pneumologista': 'fa-lungs',
        'Endocrinologista': 'fa-pills',
        'Gastroenterologista': 'fa-stomach',
        'Hepatologista': 'fa-liver',
        'Dermatologista': 'fa-allergies',
        'Oftalmologista': 'fa-eye',
        'Ortopedista': 'fa-walking',
        'Psiquiatra': 'fa-head-side-brain',
        'Neuropediatra': 'fa-child',
        'Urologista': 'fa-male',
        'Nefrologista': 'fa-kidneys',
    };

    const specialists = ci.especialistas || [];
    if (specialists.length > 0) {
        specialists.forEach(esp => {
            const card = document.createElement('div');
            card.className = 'specialist-chip';

            // Encontrar ícone correspondente
            let icon = 'fa-user-md';
            for (const [key, val] of Object.entries(specialistIcons)) {
                if (esp.toLowerCase().includes(key.toLowerCase())) {
                    icon = val;
                    break;
                }
            }

            card.innerHTML = `<i class="fas ${icon}"></i><span>${esp}</span>`;
            specialistsGrid.appendChild(card);
        });
    } else {
        specialistsGrid.innerHTML = '<p class="no-data">Consulte um médico generalista para orientação inicial.</p>';
    }

    // Exams
    const examsList = document.getElementById('exams-list');
    examsList.innerHTML = '';
    const exams = ci.exames || [];
    if (exams.length > 0) {
        exams.forEach(exam => {
            const li = document.createElement('li');
            li.innerHTML = `<i class="fas fa-flask-vial"></i><span>${exam}</span>`;
            examsList.appendChild(li);
        });
    } else {
        examsList.innerHTML = '<li><i class="fas fa-info-circle"></i><span>Consulte um especialista para solicitação de exames.</span></li>';
    }

    // Clinical note
    const clinicalNote = document.getElementById('clinical-note');
    const clinicalNoteText = document.getElementById('clinical-note-text');
    if (ci.nota_clinica) {
        clinicalNoteText.textContent = ci.nota_clinica;
        clinicalNote.style.display = 'flex';
    } else {
        clinicalNote.style.display = 'none';
    }

    // Mostrar resultados
    resultsSection.style.display = 'block';

    // Scroll para resultados
    resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });

    // Animar após render
    requestAnimationFrame(() => {
        setTimeout(() => {
            progressCircle.style.strokeDashoffset = offset;
            animateNumber(probNumber, 0, probability, 1200);
        }, 100);
    });
}

function animateNumber(element, start, end, duration) {
    const startTime = performance.now();
    const diff = end - start;

    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);

        // Easing: ease-out-cubic
        const eased = 1 - Math.pow(1 - progress, 3);
        const current = start + diff * eased;

        element.textContent = current.toFixed(1);

        if (progress < 1) {
            requestAnimationFrame(update);
        } else {
            element.textContent = end.toFixed(1);
        }
    }

    requestAnimationFrame(update);
}
