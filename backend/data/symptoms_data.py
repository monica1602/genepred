"""
Sintomas por Doença Genética

Cada doença tem uma lista de sintomas possíveis com ícone e peso.
O peso indica o quanto o sintoma aumenta a probabilidade calculada
quando presente no paciente avaliado.

Formato: { "doenca_id": { "sintomas": [ { "id", "label", "icone", "peso" } ] } }
"""

# Peso: fração de ajuste sobre a probabilidade final (ex: 0.12 = +12% relativo)
DISEASE_SYMPTOMS = {

    # ================================================================
    # CÂNCERES HEREDITÁRIOS
    # ================================================================

    "cancer_mama_brca1": {
        "sintomas": [
            {"id": "nodulo_mama", "label": "Nódulo ou caroço na mama", "icone": "fa-circle-dot", "peso": 0.20},
            {"id": "alteracao_pele_mama", "label": "Alteração na pele ou mamilo", "icone": "fa-hand-dots", "peso": 0.15},
            {"id": "secrecao_mamilo", "label": "Secreção no mamilo", "icone": "fa-droplet", "peso": 0.12},
            {"id": "dor_mama", "label": "Dor persistente na mama", "icone": "fa-bolt", "peso": 0.08},
            {"id": "nodulo_axilar", "label": "Nódulo na axila", "icone": "fa-circle-dot", "peso": 0.18},
        ],
    },
    "cancer_mama_brca2": {
        "sintomas": [
            {"id": "nodulo_mama", "label": "Nódulo ou caroço na mama", "icone": "fa-circle-dot", "peso": 0.20},
            {"id": "alteracao_pele_mama", "label": "Alteração na pele ou mamilo", "icone": "fa-hand-dots", "peso": 0.15},
            {"id": "secrecao_mamilo", "label": "Secreção no mamilo", "icone": "fa-droplet", "peso": 0.12},
            {"id": "nodulo_axilar", "label": "Nódulo na axila", "icone": "fa-circle-dot", "peso": 0.18},
        ],
    },
    "cancer_ovario_brca": {
        "sintomas": [
            {"id": "dor_pelvica", "label": "Dor ou pressão pélvica", "icone": "fa-bolt", "peso": 0.15},
            {"id": "distensao_abdominal", "label": "Distensão abdominal persistente", "icone": "fa-circle", "peso": 0.15},
            {"id": "saciedade_precoce", "label": "Saciedade precoce ao comer", "icone": "fa-utensils", "peso": 0.10},
            {"id": "alteracao_intestinal", "label": "Alteração intestinal sem causa aparente", "icone": "fa-toilet", "peso": 0.08},
            {"id": "sangramento_vaginal", "label": "Sangramento vaginal fora do ciclo", "icone": "fa-droplet", "peso": 0.18},
        ],
    },
    "cancer_prostata": {
        "sintomas": [
            {"id": "dificuldade_urinar", "label": "Dificuldade para urinar ou jato fraco", "icone": "fa-droplet", "peso": 0.15},
            {"id": "sangue_urina", "label": "Sangue na urina (hematúria)", "icone": "fa-droplet", "peso": 0.20},
            {"id": "dor_ossos", "label": "Dor óssea (coluna ou quadril)", "icone": "fa-bone", "peso": 0.18},
            {"id": "urgencia_urinaria", "label": "Urgência urinária frequente", "icone": "fa-clock", "peso": 0.10},
        ],
    },
    "sindrome_lynch": {
        "sintomas": [
            {"id": "sangue_fezes", "label": "Sangue nas fezes", "icone": "fa-droplet", "peso": 0.22},
            {"id": "alteracao_habito_intestinal", "label": "Mudança persistente no hábito intestinal", "icone": "fa-toilet", "peso": 0.15},
            {"id": "dor_abdominal", "label": "Dor abdominal recorrente", "icone": "fa-bolt", "peso": 0.12},
            {"id": "perda_peso", "label": "Perda de peso não intencional", "icone": "fa-weight-scale", "peso": 0.18},
            {"id": "anemia", "label": "Anemia (fraqueza, palidez)", "icone": "fa-face-tired", "peso": 0.12},
        ],
    },
    "polipose_adenomatosa": {
        "sintomas": [
            {"id": "sangue_fezes", "label": "Sangue nas fezes", "icone": "fa-droplet", "peso": 0.22},
            {"id": "diarreia_cronica", "label": "Diarreia crônica", "icone": "fa-toilet", "peso": 0.15},
            {"id": "dor_abdominal", "label": "Cólicas abdominais frequentes", "icone": "fa-bolt", "peso": 0.12},
            {"id": "anemia", "label": "Anemia inexplicada", "icone": "fa-face-tired", "peso": 0.12},
        ],
    },
    "melanoma_familiar": {
        "sintomas": [
            {"id": "lesao_pele_suspeita", "label": "Lesão pigmentada nova ou em crescimento", "icone": "fa-circle", "peso": 0.25},
            {"id": "nevo_irregular", "label": "Nevo com bordas irregulares ou cores variadas", "icone": "fa-circle-half-stroke", "peso": 0.22},
            {"id": "nevo_sangrante", "label": "Nevo que sangra ou coça", "icone": "fa-droplet", "peso": 0.20},
            {"id": "lesao_nao_cicatriza", "label": "Ferida na pele que não cicatriza", "icone": "fa-bandage", "peso": 0.18},
        ],
    },
    "li_fraumeni": {
        "sintomas": [
            {"id": "tumor_adrenal", "label": "Tumor adrenal detectado", "icone": "fa-circle-dot", "peso": 0.25},
            {"id": "sarcoma_osseo", "label": "Dor óssea intensa ou tumor ósseo", "icone": "fa-bone", "peso": 0.22},
            {"id": "tumor_cerebral", "label": "Cefaleia intensa progressiva ou convulsão", "icone": "fa-brain", "peso": 0.20},
            {"id": "nodulo_mama_jovem", "label": "Nódulo mamário em jovem (< 30 anos)", "icone": "fa-circle-dot", "peso": 0.20},
        ],
    },

    # ================================================================
    # DOENÇAS AUTOIMUNES
    # ================================================================

    "lupus": {
        "sintomas": [
            {"id": "erupcao_malar", "label": "Erupção em borboleta no rosto", "icone": "fa-face-smile", "peso": 0.22},
            {"id": "fotossensibilidade", "label": "Sensibilidade excessiva ao sol", "icone": "fa-sun", "peso": 0.15},
            {"id": "dor_articular", "label": "Dor e inchaço nas articulações", "icone": "fa-hand", "peso": 0.15},
            {"id": "fadiga_intensa", "label": "Fadiga intensa persistente", "icone": "fa-battery-quarter", "peso": 0.12},
            {"id": "queda_cabelo", "label": "Queda de cabelo acentuada", "icone": "fa-scissors", "peso": 0.10},
            {"id": "febre_recorrente", "label": "Febre sem causa aparente", "icone": "fa-thermometer", "peso": 0.12},
        ],
    },
    "artrite_reumatoide": {
        "sintomas": [
            {"id": "dor_articular", "label": "Dor e inchaço simétrico nas articulações", "icone": "fa-hand", "peso": 0.20},
            {"id": "rigidez_matinal", "label": "Rigidez matinal > 1 hora", "icone": "fa-clock", "peso": 0.22},
            {"id": "nodulos_reumatoides", "label": "Nódulos sob a pele", "icone": "fa-circle-dot", "peso": 0.15},
            {"id": "fadiga_intensa", "label": "Fadiga e mal-estar geral", "icone": "fa-battery-quarter", "peso": 0.10},
        ],
    },
    "diabetes_tipo1": {
        "sintomas": [
            {"id": "poliuria", "label": "Urinar muito (poliúria)", "icone": "fa-droplet", "peso": 0.18},
            {"id": "polidipsia", "label": "Sede excessiva (polidipsia)", "icone": "fa-glass-water", "peso": 0.18},
            {"id": "perda_peso", "label": "Perda de peso sem dieta", "icone": "fa-weight-scale", "peso": 0.18},
            {"id": "fadiga_intensa", "label": "Cansaço e fraqueza intensa", "icone": "fa-battery-quarter", "peso": 0.12},
            {"id": "visao_turva", "label": "Visão turva", "icone": "fa-eye-low-vision", "peso": 0.10},
        ],
    },
    "esclerose_multipla": {
        "sintomas": [
            {"id": "fraqueza_membros", "label": "Fraqueza ou dormência em membros", "icone": "fa-person-walking", "peso": 0.18},
            {"id": "visao_dupla", "label": "Visão dupla ou borrada (neurite óptica)", "icone": "fa-eye", "peso": 0.20},
            {"id": "desequilibrio", "label": "Dificuldade de equilíbrio e coordenação", "icone": "fa-person-falling", "peso": 0.18},
            {"id": "fadiga_intensa", "label": "Fadiga desproporcional", "icone": "fa-battery-quarter", "peso": 0.12},
            {"id": "espasmos_musculares", "label": "Espasmos ou rigidez muscular", "icone": "fa-bolt", "peso": 0.15},
        ],
    },
    "doenca_celica": {
        "sintomas": [
            {"id": "diarreia_cronica", "label": "Diarreia crônica após consumo de glúten", "icone": "fa-toilet", "peso": 0.22},
            {"id": "distensao_abdominal", "label": "Distensão abdominal e gases", "icone": "fa-circle", "peso": 0.15},
            {"id": "perda_peso", "label": "Perda de peso e desnutrição", "icone": "fa-weight-scale", "peso": 0.18},
            {"id": "anemia", "label": "Anemia ferropriva sem causa aparente", "icone": "fa-face-tired", "peso": 0.15},
            {"id": "dermatite_herpetiforme", "label": "Erupção cutânea pruriginosa (dermatite herpetiforme)", "icone": "fa-hand-dots", "peso": 0.20},
        ],
    },
    "hashimoto": {
        "sintomas": [
            {"id": "fadiga_intensa", "label": "Fadiga e sonolência excessiva", "icone": "fa-battery-quarter", "peso": 0.15},
            {"id": "ganho_peso", "label": "Ganho de peso inexplicado", "icone": "fa-weight-scale", "peso": 0.12},
            {"id": "pele_seca", "label": "Pele seca e queda de cabelo", "icone": "fa-scissors", "peso": 0.10},
            {"id": "intolerancia_frio", "label": "Intolerância ao frio", "icone": "fa-snowflake", "peso": 0.12},
            {"id": "bocio", "label": "Bócio (aumento da tireoide)", "icone": "fa-circle-dot", "peso": 0.18},
        ],
    },
    "doenca_crohn": {
        "sintomas": [
            {"id": "dor_abdominal", "label": "Dor abdominal em cólica intensa", "icone": "fa-bolt", "peso": 0.20},
            {"id": "diarreia_cronica", "label": "Diarreia crônica (às vezes com sangue)", "icone": "fa-toilet", "peso": 0.20},
            {"id": "perda_peso", "label": "Perda de peso e desnutrição", "icone": "fa-weight-scale", "peso": 0.15},
            {"id": "febre_recorrente", "label": "Febre recorrente de baixo grau", "icone": "fa-thermometer", "peso": 0.12},
            {"id": "fistula_anal", "label": "Fístula ou abscesso perianal", "icone": "fa-circle-dot", "peso": 0.18},
        ],
    },
    "espondilite_anquilosante": {
        "sintomas": [
            {"id": "dor_lombar_cronica", "label": "Dor lombar crônica (piora ao repouso)", "icone": "fa-bolt", "peso": 0.22},
            {"id": "rigidez_matinal", "label": "Rigidez matinal > 30 minutos", "icone": "fa-clock", "peso": 0.20},
            {"id": "dor_sacroiliaca", "label": "Dor na região sacroilíaca (nádega)", "icone": "fa-bolt", "peso": 0.20},
            {"id": "fadiga_intensa", "label": "Fadiga persistente", "icone": "fa-battery-quarter", "peso": 0.10},
            {"id": "uveite", "label": "Inflamação ocular (uveíte)", "icone": "fa-eye", "peso": 0.15},
        ],
    },

    # ================================================================
    # DOENÇAS GENÉTICAS RARAS
    # ================================================================

    "huntington": {
        "sintomas": [
            {"id": "movimentos_involuntarios", "label": "Movimentos involuntários (coreia)", "icone": "fa-person-walking", "peso": 0.25},
            {"id": "alteracao_cognitiva", "label": "Dificuldade de memória e concentração", "icone": "fa-brain", "peso": 0.20},
            {"id": "alteracao_psiquiatrica", "label": "Alterações de humor ou comportamento", "icone": "fa-face-sad-tear", "peso": 0.18},
            {"id": "dificuldade_fala", "label": "Dificuldade para falar ou engolir", "icone": "fa-comment-slash", "peso": 0.15},
            {"id": "perda_equilibrio", "label": "Perda de equilíbrio e coordenação", "icone": "fa-person-falling", "peso": 0.15},
        ],
    },
    "fibrose_cistica": {
        "sintomas": [
            {"id": "tosse_cronica", "label": "Tosse crônica com muco espesso", "icone": "fa-lungs-virus", "peso": 0.22},
            {"id": "infeccoes_respiratorias", "label": "Infecções pulmonares frequentes", "icone": "fa-virus", "peso": 0.20},
            {"id": "insuficiencia_pancreatica", "label": "Fezes gordurosas, má absorção", "icone": "fa-toilet", "peso": 0.18},
            {"id": "suor_salgado", "label": "Suor muito salgado", "icone": "fa-droplet", "peso": 0.20},
            {"id": "baixo_crescimento", "label": "Baixo peso e crescimento deficiente", "icone": "fa-child", "peso": 0.12},
        ],
    },
    "anemia_falciforme": {
        "sintomas": [
            {"id": "crises_dor", "label": "Crises de dor intensa (ossos, peito, abdômen)", "icone": "fa-bolt", "peso": 0.25},
            {"id": "anemia", "label": "Anemia (palidez, cansaço extremo)", "icone": "fa-face-tired", "peso": 0.22},
            {"id": "ictericia", "label": "Icterícia (amarelamento da pele/olhos)", "icone": "fa-circle", "peso": 0.18},
            {"id": "infeccoes_frequentes", "label": "Infecções frequentes e graves", "icone": "fa-virus", "peso": 0.15},
            {"id": "inchaço_maos_pes", "label": "Inchaço doloroso das mãos e pés (dactilite)", "icone": "fa-hand", "peso": 0.20},
        ],
    },
    "hemofilia_a": {
        "sintomas": [
            {"id": "sangramentos_excessivos", "label": "Sangramentos excessivos após pequenos cortes", "icone": "fa-droplet", "peso": 0.25},
            {"id": "hemartroses", "label": "Inchaço e dor articular espontânea (hemartrose)", "icone": "fa-hand", "peso": 0.25},
            {"id": "hematomas_faceis", "label": "Hematomas sem trauma significativo", "icone": "fa-circle-half-stroke", "peso": 0.20},
            {"id": "sangramento_prolongado", "label": "Sangramento prolongado após extração dentária", "icone": "fa-tooth", "peso": 0.18},
        ],
    },
    "hemofilia_b": {
        "sintomas": [
            {"id": "sangramentos_excessivos", "label": "Sangramentos excessivos após pequenos cortes", "icone": "fa-droplet", "peso": 0.25},
            {"id": "hemartroses", "label": "Inchaço e dor articular espontânea (hemartrose)", "icone": "fa-hand", "peso": 0.25},
            {"id": "hematomas_faceis", "label": "Hematomas sem trauma significativo", "icone": "fa-circle-half-stroke", "peso": 0.20},
        ],
    },
    "duchenne": {
        "sintomas": [
            {"id": "fraqueza_muscular_proximal", "label": "Fraqueza muscular progressiva (pernas/quadril)", "icone": "fa-person-walking", "peso": 0.25},
            {"id": "dificuldade_subir_escada", "label": "Dificuldade para subir escadas ou levantar do chão", "icone": "fa-stairs", "peso": 0.22},
            {"id": "marcha_pato", "label": "Marcha anserina (marcha de pato)", "icone": "fa-person-walking", "peso": 0.20},
            {"id": "panturrilhas_aumentadas", "label": "Panturrilhas visivelmente aumentadas", "icone": "fa-circle", "peso": 0.20},
            {"id": "sinal_gowers", "label": "Usa os braços para levantar do chão (sinal de Gowers)", "icone": "fa-hands", "peso": 0.22},
        ],
    },
    "marfan": {
        "sintomas": [
            {"id": "alta_estatura", "label": "Estatura muito alta e membros longos", "icone": "fa-ruler-vertical", "peso": 0.15},
            {"id": "dor_toracica", "label": "Dor torácica ou nas costas", "icone": "fa-bolt", "peso": 0.20},
            {"id": "lens_subluxada", "label": "Visão turva, cristalino fora do lugar", "icone": "fa-eye", "peso": 0.20},
            {"id": "escoliose", "label": "Curvatura da coluna (escoliose)", "icone": "fa-person", "peso": 0.12},
            {"id": "hipermobilidade", "label": "Articulações muito flexíveis (hipermobilidade)", "icone": "fa-hand", "peso": 0.12},
        ],
    },
    "doenca_wilson": {
        "sintomas": [
            {"id": "ictericia", "label": "Icterícia (pele e olhos amarelados)", "icone": "fa-circle", "peso": 0.18},
            {"id": "tremores", "label": "Tremores nas mãos", "icone": "fa-hand", "peso": 0.20},
            {"id": "alteracao_psiquiatrica", "label": "Alterações de comportamento ou psicose", "icone": "fa-brain", "peso": 0.18},
            {"id": "dificuldade_fala", "label": "Dificuldade para falar ou engolir", "icone": "fa-comment-slash", "peso": 0.15},
            {"id": "dor_abdominal", "label": "Dor abdominal e hepatomegalia", "icone": "fa-bolt", "peso": 0.15},
        ],
    },
    "talassemia": {
        "sintomas": [
            {"id": "anemia", "label": "Anemia grave (extrema palidez e fraqueza)", "icone": "fa-face-tired", "peso": 0.25},
            {"id": "ictericia", "label": "Icterícia", "icone": "fa-circle", "peso": 0.18},
            {"id": "esplenomegalia", "label": "Abdômen aumentado (esplenomegalia)", "icone": "fa-circle", "peso": 0.18},
            {"id": "baixo_crescimento", "label": "Crescimento retardado em crianças", "icone": "fa-child", "peso": 0.15},
            {"id": "deformidade_ossea", "label": "Deformidades ósseas faciais", "icone": "fa-circle-dot", "peso": 0.15},
        ],
    },
    "gaucher": {
        "sintomas": [
            {"id": "esplenomegalia", "label": "Baço muito aumentado (esplenomegalia)", "icone": "fa-circle", "peso": 0.22},
            {"id": "dor_ossea", "label": "Dor óssea intensa ou fraturas", "icone": "fa-bone", "peso": 0.20},
            {"id": "anemia", "label": "Anemia e trombocitopenia (hematomas fáceis)", "icone": "fa-face-tired", "peso": 0.18},
            {"id": "fadiga_intensa", "label": "Fadiga extrema", "icone": "fa-battery-quarter", "peso": 0.12},
        ],
    },
    "tay_sachs": {
        "sintomas": [
            {"id": "regressao_desenvolvimento", "label": "Regressão do desenvolvimento neuromotor", "icone": "fa-child", "peso": 0.25},
            {"id": "hipersensibilidade_sonora", "label": "Reação exagerada a sons (sobressalto)", "icone": "fa-ear-listen", "peso": 0.22},
            {"id": "fraqueza_muscular", "label": "Fraqueza muscular progressiva", "icone": "fa-person-walking", "peso": 0.20},
            {"id": "convulsoes", "label": "Convulsões", "icone": "fa-bolt", "peso": 0.20},
        ],
    },
    "ataxia_friedreich": {
        "sintomas": [
            {"id": "ataxia_marcha", "label": "Dificuldade para caminhar (marcha instável)", "icone": "fa-person-falling", "peso": 0.25},
            {"id": "perda_equilibrio", "label": "Perda de equilíbrio e coordenação", "icone": "fa-person-falling", "peso": 0.22},
            {"id": "cardiomiopatia_sx", "label": "Palpitações ou dispneia (cardiomiopatia)", "icone": "fa-heart-pulse", "peso": 0.20},
            {"id": "escoliose", "label": "Escoliose progressiva", "icone": "fa-person", "peso": 0.12},
            {"id": "perda_sensibilidade", "label": "Perda de sensibilidade nos pés/pernas", "icone": "fa-hand", "peso": 0.18},
        ],
    },
    "neurofibromatose": {
        "sintomas": [
            {"id": "manchas_cafe_leite", "label": "Manchas café-com-leite na pele (≥ 6)", "icone": "fa-circle-half-stroke", "peso": 0.25},
            {"id": "neurofibromas", "label": "Nódulos sob a pele (neurofibromas)", "icone": "fa-circle-dot", "peso": 0.22},
            {"id": "sardas_axilares", "label": "Sardas na axila ou virilha", "icone": "fa-hand-dots", "peso": 0.20},
            {"id": "nodulos_lisch", "label": "Nódulos de Lisch (olho — diagnóstico oftalmológico)", "icone": "fa-eye", "peso": 0.20},
        ],
    },
    "esclerose_tuberosa": {
        "sintomas": [
            {"id": "convulsoes", "label": "Convulsões (especialmente em crianças)", "icone": "fa-bolt", "peso": 0.22},
            {"id": "manchas_pele", "label": "Manchas brancas ou lesões na pele", "icone": "fa-circle-half-stroke", "peso": 0.20},
            {"id": "angiofibromas_faciais", "label": "Angiofibromas faciais (lesões avermelhadas)", "icone": "fa-face-smile", "peso": 0.20},
            {"id": "atraso_desenvolvimento", "label": "Atraso de desenvolvimento ou autismo", "icone": "fa-child", "peso": 0.15},
        ],
    },
    "osteogenese_imperfeita": {
        "sintomas": [
            {"id": "fraturas_frequentes", "label": "Fraturas frequentes com trauma mínimo", "icone": "fa-bone", "peso": 0.30},
            {"id": "escleras_azuis", "label": "Escleras azuladas (branco do olho azul)", "icone": "fa-eye", "peso": 0.22},
            {"id": "perda_auditiva", "label": "Perda auditiva progressiva", "icone": "fa-ear-listen", "peso": 0.15},
            {"id": "baixa_estatura", "label": "Baixa estatura e deformidades ósseas", "icone": "fa-ruler-vertical", "peso": 0.15},
        ],
    },
    "ehlers_danlos": {
        "sintomas": [
            {"id": "hipermobilidade", "label": "Articulações hipermóveis com luxações frequentes", "icone": "fa-hand", "peso": 0.22},
            {"id": "pele_hiperelastica", "label": "Pele hiperelástica (estica excessivamente)", "icone": "fa-hand-dots", "peso": 0.20},
            {"id": "cicatrizes_largas", "label": "Cicatrizes alargadas ou frágeis", "icone": "fa-bandage", "peso": 0.18},
            {"id": "dor_cronica", "label": "Dor crônica musculoesquelética", "icone": "fa-bolt", "peso": 0.15},
        ],
    },
    "fabry": {
        "sintomas": [
            {"id": "dor_ardente_maos_pes", "label": "Dor ardente nas mãos e pés (acroparestesia)", "icone": "fa-fire", "peso": 0.25},
            {"id": "intolerancia_calor", "label": "Intolerância ao calor ou exercício", "icone": "fa-temperature-high", "peso": 0.20},
            {"id": "angioqueratomas", "label": "Lesões avermelhadas na pele (angioqueratomas)", "icone": "fa-hand-dots", "peso": 0.22},
            {"id": "proteinuria", "label": "Proteína na urina", "icone": "fa-droplet", "peso": 0.15},
            {"id": "avc_jovem", "label": "AVC ou AIT em jovem (< 45 anos)", "icone": "fa-brain", "peso": 0.22},
        ],
    },
    "pompe": {
        "sintomas": [
            {"id": "fraqueza_muscular", "label": "Fraqueza muscular proximal progressiva", "icone": "fa-person-walking", "peso": 0.25},
            {"id": "dispneia", "label": "Falta de ar e insuficiência respiratória", "icone": "fa-lungs", "peso": 0.22},
            {"id": "dificuldade_deglutir", "label": "Dificuldade para engolir", "icone": "fa-comment-slash", "peso": 0.15},
            {"id": "cardiomegalia_sx", "label": "Coração aumentado (cardiomegalia — forma infantil)", "icone": "fa-heart", "peso": 0.20},
        ],
    },
    "rett": {
        "sintomas": [
            {"id": "perda_habilidades_maos", "label": "Perda de habilidades manuais adquiridas", "icone": "fa-hands", "peso": 0.28},
            {"id": "movimentos_esterotipados", "label": "Movimentos estereotipados das mãos (torção, lavagem)", "icone": "fa-hand", "peso": 0.25},
            {"id": "regressao_linguagem", "label": "Regressão da fala e linguagem", "icone": "fa-comment-slash", "peso": 0.25},
            {"id": "convulsoes", "label": "Convulsões", "icone": "fa-bolt", "peso": 0.18},
            {"id": "respiracao_irregular", "label": "Respiração irregular (apneia, hiperventilação)", "icone": "fa-lungs", "peso": 0.18},
        ],
    },
    "noonan": {
        "sintomas": [
            {"id": "baixa_estatura", "label": "Baixa estatura", "icone": "fa-ruler-vertical", "peso": 0.15},
            {"id": "dismorfia_facial", "label": "Características faciais típicas (orelhas baixas, pescoço curto)", "icone": "fa-face-smile", "peso": 0.20},
            {"id": "criptorquidia", "label": "Criptorquidia (testículos não descidos)", "icone": "fa-circle-dot", "peso": 0.18},
            {"id": "sopro_cardiaco", "label": "Sopro cardíaco (estenose pulmonar)", "icone": "fa-heart-pulse", "peso": 0.22},
            {"id": "dificuldade_alimentacao", "label": "Dificuldade de alimentação na infância", "icone": "fa-utensils", "peso": 0.12},
        ],
    },
    "prader_willi": {
        "sintomas": [
            {"id": "hipotonia_neonatal", "label": "Hipotonia grave ao nascer (bebê molinho)", "icone": "fa-baby", "peso": 0.25},
            {"id": "hiperfagia", "label": "Apetite insaciável e obesidade progressiva", "icone": "fa-utensils", "peso": 0.25},
            {"id": "baixa_estatura", "label": "Baixa estatura e mãos/pés pequenos", "icone": "fa-ruler-vertical", "peso": 0.15},
            {"id": "hipogonadismo", "label": "Hipogonadismo (desenvolvimento sexual incompleto)", "icone": "fa-circle-dot", "peso": 0.18},
            {"id": "atraso_intelectual", "label": "Atraso intelectual leve-moderado", "icone": "fa-brain", "peso": 0.15},
        ],
    },
    "williams": {
        "sintomas": [
            {"id": "sopro_cardiaco", "label": "Sopro cardíaco (estenose aórtica supravalvar)", "icone": "fa-heart-pulse", "peso": 0.22},
            {"id": "hipercalcemia_sx", "label": "Irritabilidade extrema no bebê (hipercalcemia)", "icone": "fa-baby", "peso": 0.18},
            {"id": "atraso_desenvolvimento", "label": "Atraso de desenvolvimento e linguagem", "icone": "fa-child", "peso": 0.15},
            {"id": "personalidade_hiperamigavel", "label": "Personalidade extremamente amigável", "icone": "fa-face-grin", "peso": 0.12},
            {"id": "dismorfia_facial", "label": "Características faciais típicas (face élfica)", "icone": "fa-face-smile", "peso": 0.15},
        ],
    },
    "acondroplasia": {
        "sintomas": [
            {"id": "baixa_estatura", "label": "Baixa estatura desproporcionada (membros curtos)", "icone": "fa-ruler-vertical", "peso": 0.30},
            {"id": "macrocefalia", "label": "Cabeça aumentada (macrocefalia)", "icone": "fa-circle", "peso": 0.20},
            {"id": "lordose_lombar", "label": "Curvatura lombar acentuada (lordose)", "icone": "fa-person", "peso": 0.15},
            {"id": "apneia_sono", "label": "Apneia do sono", "icone": "fa-moon", "peso": 0.15},
        ],
    },

    # ================================================================
    # CARDIOVASCULARES
    # ================================================================

    "cardiomiopatia_hipertrofica": {
        "sintomas": [
            {"id": "dispneia_esforco", "label": "Falta de ar ao esforço", "icone": "fa-lungs", "peso": 0.18},
            {"id": "sincope", "label": "Desmaio ou pré-síncope ao exercício", "icone": "fa-person-falling", "peso": 0.25},
            {"id": "palpitacoes", "label": "Palpitações ou batimentos irregulares", "icone": "fa-heart-pulse", "peso": 0.20},
            {"id": "dor_toracica", "label": "Dor torácica ao esforço", "icone": "fa-bolt", "peso": 0.18},
            {"id": "sopro_cardiaco", "label": "Sopro cardíaco", "icone": "fa-heart-pulse", "peso": 0.15},
        ],
    },
    "cardiomiopatia_dilatada": {
        "sintomas": [
            {"id": "dispneia_esforco", "label": "Falta de ar progressiva", "icone": "fa-lungs", "peso": 0.20},
            {"id": "edema_membros", "label": "Inchaço nas pernas (edema)", "icone": "fa-person-walking", "peso": 0.18},
            {"id": "fadiga_intensa", "label": "Fadiga extrema", "icone": "fa-battery-quarter", "peso": 0.15},
            {"id": "palpitacoes", "label": "Palpitações ou arritmias", "icone": "fa-heart-pulse", "peso": 0.20},
            {"id": "sincope", "label": "Desmaio ou pré-síncope", "icone": "fa-person-falling", "peso": 0.20},
        ],
    },
    "sindrome_qt_longo": {
        "sintomas": [
            {"id": "sincope", "label": "Desmaio (especialmente ao exercício ou susto)", "icone": "fa-person-falling", "peso": 0.28},
            {"id": "palpitacoes", "label": "Palpitações e arritmias", "icone": "fa-heart-pulse", "peso": 0.22},
            {"id": "convulsoes", "label": "Convulsões sem causa neurológica", "icone": "fa-bolt", "peso": 0.20},
            {"id": "morte_subita_familiar", "label": "Morte súbita em jovem na família", "icone": "fa-circle-exclamation", "peso": 0.25},
        ],
    },
    "sindrome_brugada": {
        "sintomas": [
            {"id": "sincope", "label": "Desmaio inexplicado", "icone": "fa-person-falling", "peso": 0.25},
            {"id": "palpitacoes", "label": "Palpitações noturnas", "icone": "fa-heart-pulse", "peso": 0.20},
            {"id": "morte_subita_familiar", "label": "Morte súbita em familiar jovem", "icone": "fa-circle-exclamation", "peso": 0.25},
            {"id": "febre_gatilho", "label": "Sintomas pioram com febre", "icone": "fa-thermometer", "peso": 0.15},
        ],
    },
    "hipercolesterolemia_familiar": {
        "sintomas": [
            {"id": "xantomas", "label": "Xantomas (nódulos amarelados nos tendões/cotovelos)", "icone": "fa-circle-dot", "peso": 0.25},
            {"id": "xantelasmas", "label": "Xantelasmas (depósitos amarelados nas pálpebras)", "icone": "fa-eye", "peso": 0.22},
            {"id": "arco_corneal", "label": "Arco corneal antes dos 45 anos", "icone": "fa-eye", "peso": 0.20},
            {"id": "dor_toracica", "label": "Dor torácica (angina)", "icone": "fa-bolt", "peso": 0.18},
        ],
    },
    "aneurisma_aorta_familiar": {
        "sintomas": [
            {"id": "dor_costas_intensa", "label": "Dor intensa nas costas ou abdômen (emergência)", "icone": "fa-bolt", "peso": 0.30},
            {"id": "pulsacao_abdominal", "label": "Pulsação no abdômen", "icone": "fa-circle-dot", "peso": 0.22},
            {"id": "dor_toracica", "label": "Dor torácica com irradiação", "icone": "fa-bolt", "peso": 0.20},
        ],
    },

    # ================================================================
    # NEUROLÓGICAS
    # ================================================================

    "alzheimer_familiar": {
        "sintomas": [
            {"id": "perda_memoria", "label": "Perda de memória recente progressiva", "icone": "fa-brain", "peso": 0.25},
            {"id": "desorientacao", "label": "Desorientação no tempo e espaço", "icone": "fa-compass", "peso": 0.22},
            {"id": "dificuldade_linguagem", "label": "Dificuldade para encontrar palavras", "icone": "fa-comment-slash", "peso": 0.18},
            {"id": "alteracao_personalidade", "label": "Alteração de personalidade ou comportamento", "icone": "fa-face-sad-tear", "peso": 0.15},
        ],
    },
    "parkinson_familiar": {
        "sintomas": [
            {"id": "tremor_repouso", "label": "Tremor em repouso (mãos, queixo)", "icone": "fa-hand", "peso": 0.25},
            {"id": "rigidez_muscular", "label": "Rigidez muscular (braços, pescoço)", "icone": "fa-person-walking", "peso": 0.20},
            {"id": "bradicinesia", "label": "Lentidão dos movimentos (bradicinesia)", "icone": "fa-person-walking", "peso": 0.22},
            {"id": "alteracao_marcha", "label": "Dificuldade para iniciar caminhada, passos curtos", "icone": "fa-person-walking", "peso": 0.18},
            {"id": "hiposmia", "label": "Perda ou redução do olfato", "icone": "fa-nose", "peso": 0.12},
        ],
    },
    "ela_familiar": {
        "sintomas": [
            {"id": "fraqueza_membros", "label": "Fraqueza muscular progressiva (braços ou pernas)", "icone": "fa-person-walking", "peso": 0.25},
            {"id": "fasciculacoes", "label": "Espasmos/fasciculações musculares visíveis", "icone": "fa-bolt", "peso": 0.22},
            {"id": "disfagia", "label": "Dificuldade para engolir (disfagia)", "icone": "fa-comment-slash", "peso": 0.20},
            {"id": "disfonia", "label": "Voz arrastada ou anasalada", "icone": "fa-microphone-slash", "peso": 0.18},
            {"id": "dispneia", "label": "Falta de ar progressiva", "icone": "fa-lungs", "peso": 0.20},
        ],
    },
    "epilepsia_genetica": {
        "sintomas": [
            {"id": "convulsoes", "label": "Crises convulsivas", "icone": "fa-bolt", "peso": 0.30},
            {"id": "ausencias", "label": "Episódios de ausência (ficar parado olhando fixo)", "icone": "fa-circle", "peso": 0.22},
            {"id": "queda_subita", "label": "Quedas súbitas sem perda de consciência (crises atônicas)", "icone": "fa-person-falling", "peso": 0.20},
            {"id": "aura_episodios", "label": "Sensações estranhas antes das crises (aura)", "icone": "fa-eye", "peso": 0.15},
        ],
    },
    "charcot_marie_tooth": {
        "sintomas": [
            {"id": "fraqueza_pe", "label": "Fraqueza e atrofia dos pés e pernas", "icone": "fa-person-walking", "peso": 0.25},
            {"id": "pe_cavo", "label": "Pé cavo (arco plantar muito alto)", "icone": "fa-shoe-prints", "peso": 0.22},
            {"id": "perda_sensibilidade", "label": "Perda de sensibilidade nos pés", "icone": "fa-hand", "peso": 0.20},
            {"id": "queda_frequente", "label": "Quedas frequentes ao caminhar", "icone": "fa-person-falling", "peso": 0.18},
        ],
    },
    "atrofia_muscular_espinhal": {
        "sintomas": [
            {"id": "hipotonia", "label": "Hipotonia grave (bebê molinho)", "icone": "fa-baby", "peso": 0.28},
            {"id": "fraqueza_muscular", "label": "Fraqueza muscular progressiva", "icone": "fa-person-walking", "peso": 0.25},
            {"id": "dificuldade_sugar", "label": "Dificuldade para sugar/engolir", "icone": "fa-comment-slash", "peso": 0.20},
            {"id": "insuficiencia_respiratoria", "label": "Insuficiência respiratória", "icone": "fa-lungs", "peso": 0.25},
        ],
    },

    # ================================================================
    # METABÓLICAS
    # ================================================================

    "diabetes_tipo2_genetico": {
        "sintomas": [
            {"id": "poliuria", "label": "Urinar muito (poliúria)", "icone": "fa-droplet", "peso": 0.15},
            {"id": "polidipsia", "label": "Sede excessiva", "icone": "fa-glass-water", "peso": 0.15},
            {"id": "fadiga_intensa", "label": "Cansaço e letargia", "icone": "fa-battery-quarter", "peso": 0.10},
            {"id": "visao_turva", "label": "Visão turva", "icone": "fa-eye-low-vision", "peso": 0.10},
            {"id": "cicatrizacao_lenta", "label": "Feridas que demoram para cicatrizar", "icone": "fa-bandage", "peso": 0.12},
        ],
    },
    "diabetes_mody": {
        "sintomas": [
            {"id": "hiperglicemia_leve", "label": "Glicemia levemente elevada em jovem (< 25 anos)", "icone": "fa-droplet", "peso": 0.22},
            {"id": "diabetes_familiar_jovens", "label": "Vários familiares com diabetes de início jovem", "icone": "fa-users", "peso": 0.20},
            {"id": "poliuria", "label": "Urinar frequentemente", "icone": "fa-droplet", "peso": 0.12},
        ],
    },
    "hemocromatose": {
        "sintomas": [
            {"id": "fadiga_intensa", "label": "Fadiga intensa e fraqueza", "icone": "fa-battery-quarter", "peso": 0.15},
            {"id": "dor_articular", "label": "Dor articular (especialmente nos dedos)", "icone": "fa-hand", "peso": 0.18},
            {"id": "pele_bronzeada", "label": "Pele bronzeada sem exposição solar", "icone": "fa-sun", "peso": 0.20},
            {"id": "diabetes_hepatite", "label": "Diabetes ou alteração hepática sem causa", "icone": "fa-circle-dot", "peso": 0.18},
            {"id": "disfuncao_sexual", "label": "Disfunção sexual ou amenorreia", "icone": "fa-circle-dot", "peso": 0.15},
        ],
    },
    "deficiencia_alfa1_antitripsina": {
        "sintomas": [
            {"id": "dispneia_precoce", "label": "Falta de ar em jovem fumante ou não fumante", "icone": "fa-lungs", "peso": 0.22},
            {"id": "enfisema_precoce", "label": "Diagnóstico de enfisema antes dos 45 anos", "icone": "fa-lungs", "peso": 0.25},
            {"id": "ictericia_neonatal", "label": "Icterícia neonatal prolongada", "icone": "fa-baby", "peso": 0.20},
            {"id": "cirrose_jovem", "label": "Cirrose hepática em jovem", "icone": "fa-circle-dot", "peso": 0.20},
        ],
    },
    "galactosemia": {
        "sintomas": [
            {"id": "ictericia_neonatal", "label": "Icterícia após início da amamentação", "icone": "fa-baby", "peso": 0.22},
            {"id": "recusa_alimentacao", "label": "Recusa alimentar e vômitos no recém-nascido", "icone": "fa-utensils", "peso": 0.20},
            {"id": "hipotonia_neonatal", "label": "Hipotonia no recém-nascido", "icone": "fa-baby", "peso": 0.18},
            {"id": "catarata_precoce", "label": "Catarata em criança pequena", "icone": "fa-eye", "peso": 0.22},
        ],
    },
    "porfiria_aguda": {
        "sintomas": [
            {"id": "dor_abdominal_intensa", "label": "Dor abdominal intensa episódica", "icone": "fa-bolt", "peso": 0.25},
            {"id": "urina_escura", "label": "Urina escura (cor de vinho/porto)", "icone": "fa-droplet", "peso": 0.25},
            {"id": "neuropatia", "label": "Dormência ou fraqueza nos membros", "icone": "fa-hand", "peso": 0.18},
            {"id": "alteracao_psiquiatrica", "label": "Confusão mental ou alucinações durante crises", "icone": "fa-brain", "peso": 0.18},
        ],
    },

    # ================================================================
    # PSIQUIÁTRICAS
    # ================================================================

    "esquizofrenia": {
        "sintomas": [
            {"id": "alucinacoes", "label": "Alucinações (ouvir ou ver coisas)", "icone": "fa-eye", "peso": 0.25},
            {"id": "delirios", "label": "Crenças delirantes", "icone": "fa-brain", "peso": 0.22},
            {"id": "pensamento_desorganizado", "label": "Pensamento desorganizado, fala incoerente", "icone": "fa-comment-slash", "peso": 0.18},
            {"id": "isolamento_social", "label": "Isolamento social progressivo", "icone": "fa-person", "peso": 0.15},
            {"id": "afeto_embotado", "label": "Embotamento afetivo (ausência de emoções)", "icone": "fa-face-meh", "peso": 0.15},
        ],
    },
    "transtorno_bipolar": {
        "sintomas": [
            {"id": "mania", "label": "Episódios de euforia extrema (mania)", "icone": "fa-face-laugh", "peso": 0.25},
            {"id": "depressao", "label": "Episódios de depressão profunda", "icone": "fa-face-sad-tear", "peso": 0.22},
            {"id": "sono_reduzido", "label": "Necessidade muito reduzida de sono na mania", "icone": "fa-moon", "peso": 0.18},
            {"id": "impulsividade", "label": "Comportamento impulsivo ou decisões precipitadas", "icone": "fa-bolt", "peso": 0.15},
        ],
    },
    "autismo_genetico": {
        "sintomas": [
            {"id": "atraso_linguagem", "label": "Atraso ou regressão da linguagem", "icone": "fa-comment-slash", "peso": 0.22},
            {"id": "dificuldade_social", "label": "Dificuldade de interação social", "icone": "fa-users-slash", "peso": 0.20},
            {"id": "comportamento_repetitivo", "label": "Comportamentos repetitivos e rituais", "icone": "fa-rotate", "peso": 0.18},
            {"id": "hipersensibilidade_sensorial", "label": "Hipersensibilidade a sons, luz ou texturas", "icone": "fa-ear-listen", "peso": 0.15},
        ],
    },
    "tdah_genetico": {
        "sintomas": [
            {"id": "desatencao", "label": "Desatenção persistente e dificuldade de concentração", "icone": "fa-brain", "peso": 0.20},
            {"id": "hiperatividade", "label": "Hiperatividade e inquietação", "icone": "fa-bolt", "peso": 0.18},
            {"id": "impulsividade", "label": "Impulsividade e dificuldade de esperar a vez", "icone": "fa-bolt", "peso": 0.18},
            {"id": "desempenho_escolar", "label": "Baixo desempenho escolar apesar de inteligência preservada", "icone": "fa-graduation-cap", "peso": 0.12},
        ],
    },
}


def get_disease_symptoms(doenca_id: str) -> list:
    """Retorna lista de sintomas para uma doença."""
    return DISEASE_SYMPTOMS.get(doenca_id, {}).get("sintomas", [])


def calcular_ajuste_sintomas(doenca_id: str, sintomas_presentes: list) -> float:
    """
    Calcula o fator de ajuste da probabilidade baseado nos sintomas relatados.
    Retorna um multiplicador (ex: 1.30 = +30% na probabilidade).
    Limitado a no máximo +60% de ajuste total para não inflar demais.
    """
    sintomas_doenca = DISEASE_SYMPTOMS.get(doenca_id, {}).get("sintomas", [])
    if not sintomas_doenca or not sintomas_presentes:
        return 1.0

    pesos_mapa = {s["id"]: s["peso"] for s in sintomas_doenca}
    ajuste_total = 0.0
    for sintoma_id in sintomas_presentes:
        if sintoma_id in pesos_mapa:
            ajuste_total += pesos_mapa[sintoma_id]

    # Cap de 60% de ajuste máximo
    ajuste_total = min(ajuste_total, 0.60)
    return 1.0 + ajuste_total
