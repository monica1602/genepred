"""
Informações Clínicas por Doença Genética

Para cada doença: exames recomendados, especialistas a consultar e urgência por nível de risco.
Urgência: "eletiva" | "prioritária" | "urgente"
"""

# Escala de urgência por nível de risco e doença
# urgencia_por_risco: { nivel_risco -> urgencia }

DISEASE_CLINICAL_INFO = {

    # ================================================================
    # CÂNCERES HEREDITÁRIOS
    # ================================================================

    "cancer_mama_brca1": {
        "exames": [
            "Teste genético BRCA1/BRCA2 (sequenciamento NGS)",
            "Ressonância Magnética (RM) de mama anual",
            "Mamografia bilateral anual (a partir dos 25-30 anos)",
            "Ultrassonografia mamária semestral",
            "Pesquisa de mutações em painel multigênico",
            "CA 125 sérico (vigilância ovariana)",
        ],
        "especialistas": [
            "Oncogeneticista",
            "Mastologista",
            "Oncologista clínico",
            "Ginecologista especializado em genética",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva",
            "Baixo": "eletiva",
            "Moderado": "prioritária",
            "Alto": "prioritária",
            "Muito Alto": "urgente",
        },
        "nota_clinica": "Portadoras de BRCA1 têm risco vitalício de ~72% para câncer de mama. Considerar quimioprofilaxia ou mastectomia profilática em casos selecionados.",
    },

    "cancer_mama_brca2": {
        "exames": [
            "Teste genético BRCA1/BRCA2 (sequenciamento NGS)",
            "Ressonância Magnética (RM) de mama anual",
            "Mamografia bilateral anual",
            "Ultrassonografia mamária semestral",
            "PSA sérico (homens com BRCA2 — risco de câncer de próstata)",
        ],
        "especialistas": [
            "Oncogeneticista",
            "Mastologista",
            "Oncologista clínico",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "prioritária", "Muito Alto": "urgente",
        },
        "nota_clinica": "BRCA2 também aumenta risco de câncer de pâncreas, próstata e melanoma em ambos os sexos.",
    },

    "cancer_ovario_brca": {
        "exames": [
            "Teste genético BRCA1/BRCA2",
            "CA 125 sérico semestral",
            "Ultrassonografia transvaginal semestral",
            "HE4 sérico",
            "Painel multigênico hereditário",
        ],
        "especialistas": [
            "Oncogeneticista",
            "Ginecologista oncológico",
            "Oncologista clínico",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Considerar salpingo-ooforectomia bilateral profilática após completar prole (idealmente entre 35-40 anos para BRCA1).",
    },

    "cancer_prostata": {
        "exames": [
            "PSA total e livre sérico anual",
            "Toque retal anual",
            "Ressonância Magnética multiparamétrica de próstata",
            "Biopsia de próstata guiada por fusão (se indicado)",
            "Teste genético BRCA2 / painel multigênico",
        ],
        "especialistas": [
            "Urologista",
            "Oncogeneticista",
            "Oncologista clínico",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "prioritária", "Muito Alto": "urgente",
        },
        "nota_clinica": "Rastreamento deve começar aos 40 anos em homens com histórico familiar forte ou mutação BRCA2.",
    },

    "melanoma_familiar": {
        "exames": [
            "Dermatoscopia digital de corpo inteiro anual",
            "Mapeamento de nevos (fotografia comparativa)",
            "Teste genético CDKN2A/CDK4",
            "Biópsia de lesões suspeitas",
            "Ultrassonografia de linfonodos (quando indicado)",
        ],
        "especialistas": [
            "Dermatologista especializado em oncologia cutânea",
            "Oncogeneticista",
            "Oncologista clínico",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "prioritária", "Muito Alto": "urgente",
        },
        "nota_clinica": "Proteção solar rigorosa e autoexame mensal são essenciais. Vigilância semestral a partir dos 18 anos.",
    },

    "sindrome_lynch": {
        "exames": [
            "Colonoscopia anual ou bianual",
            "Teste genético MMR (MLH1, MSH2, MSH6, PMS2)",
            "Instabilidade de microssatélites (MSI) em tecido tumoral",
            "Imuno-histoquímica de proteínas MMR",
            "Ultrassonografia transvaginal anual (mulheres)",
            "Urinálise com citologia anual",
        ],
        "especialistas": [
            "Oncogeneticista",
            "Gastroenterologista / Coloproctologista",
            "Ginecologista oncológico",
            "Oncologista clínico",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Risco vitalício de câncer colorretal de 50-80%. Colonoscopia a cada 1-2 anos a partir dos 20-25 anos.",
    },

    "retinoblastoma": {
        "exames": [
            "Exame oftalmológico com dilatação pupilar",
            "Retinoscopia sob anestesia (crianças)",
            "Ressonância Magnética de órbita e crânio",
            "Teste genético RB1",
            "Tomografia computadorizada de órbita",
        ],
        "especialistas": [
            "Oftalmologista pediátrico / Oncologista ocular",
            "Oncogeneticista",
            "Oncologista pediátrico",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "prioritária",
            "Moderado": "urgente", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Triagem oftalmológica obrigatória em recém-nascidos de famílias afetadas. Diagnóstico precoce é crítico para preservação da visão.",
    },

    "cancer_tireoide_medular": {
        "exames": [
            "Calcitonina sérica basal e estimulada",
            "CEA (antígeno carcinoembrionário)",
            "Teste genético RET (proto-oncogene)",
            "Ultrassonografia de tireoide",
            "Cálcio e PTH séricos (excluir hiperparatireoidismo — MEN2)",
            "Catecolaminas urinárias e metanefrinas (excluir feocromocitoma)",
        ],
        "especialistas": [
            "Endocrinologista",
            "Oncogeneticista",
            "Cirurgião de cabeça e pescoço / Cirurgião endócrino",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "prioritária",
            "Moderado": "urgente", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Tireoidectomia profilática é indicada para portadores de mutação RET de alta penetrância, idealmente na infância.",
    },

    "cancer_rim_vhl": {
        "exames": [
            "Teste genético VHL",
            "Ressonância Magnética de abdômen anual",
            "Ultrassonografia renal semestral",
            "Oftalmoscopia (hemangioblastomas retinianos)",
            "RM de crânio e coluna vertebral",
            "Catecolaminas urinárias (feocromocitoma)",
        ],
        "especialistas": [
            "Oncogeneticista",
            "Urologista / Cirurgião renal",
            "Neurologista / Neurocirurgião",
            "Oftalmologista",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Síndrome de Von Hippel-Lindau afeta múltiplos órgãos; vigilância multidisciplinar é essencial.",
    },

    "polipose_adenomatosa": {
        "exames": [
            "Colonoscopia anual (a partir dos 10-12 anos)",
            "Teste genético APC",
            "Endoscopia digestiva alta (vigilância duodenal)",
            "Radiografia de ossos longos (osteomas — Síndrome de Gardner)",
            "Ultrassonografia de tireoide",
        ],
        "especialistas": [
            "Gastroenterologista / Coloproctologista",
            "Oncogeneticista",
            "Cirurgião colorretal",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "prioritária",
            "Moderado": "urgente", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Sem tratamento, risco de câncer colorretal é de praticamente 100% até os 40 anos. Colectomia profilática é geralmente recomendada.",
    },

    "li_fraumeni": {
        "exames": [
            "Teste genético TP53",
            "Protocolo MDACC de vigilância: RM de corpo inteiro anual",
            "Colonoscopia a cada 2-5 anos",
            "Mamografia / RM mamária anual (mulheres)",
            "Dermatoscopia anual",
            "Neuroimagem anual (crianças)",
        ],
        "especialistas": [
            "Oncogeneticista",
            "Oncologista clínico",
            "Mastologista (mulheres)",
            "Neuropediatra (crianças)",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "prioritária",
            "Moderado": "urgente", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Síndrome de Li-Fraumeni implica risco de múltiplos tumores primários ao longo da vida. Evitar radioterapia quando possível.",
    },

    "cancer_pancreas_hereditario": {
        "exames": [
            "Colangiopancreatografia por Ressonância Magnética (CPRM) anual",
            "Ecoendoscopia (USE) pancreática anual",
            "CA 19-9 sérico",
            "Teste genético BRCA2, PALB2, ATM, PRSS1",
        ],
        "especialistas": [
            "Gastroenterologista",
            "Oncogeneticista",
            "Cirurgião hepatopancreático",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Vigilância recomendada a partir dos 50 anos ou 10 anos antes do caso mais jovem na família.",
    },

    "sindrome_qt_longo": {
        "exames": [
            "Eletrocardiograma (ECG) em repouso",
            "Holter 24h",
            "Teste de esforço ergométrico",
            "Teste de provocação com adrenalina ou epinefrina",
            "Teste genético KCNQ1, KCNH2, SCN5A (LQTS 1, 2, 3)",
            "Ecocardiograma",
        ],
        "especialistas": [
            "Cardiologista / Arritmologista",
            "Oncogeneticista / Geneticista clínico",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Risco de morte súbita. Evitar medicamentos que prolongam o intervalo QT. CDI pode ser indicado em casos de alto risco.",
    },

    # ================================================================
    # DOENÇAS AUTOIMUNES
    # ================================================================

    "lupus": {
        "exames": [
            "FAN (fator antinuclear) — padrão e titulação",
            "Anti-DNA dupla fita (anti-dsDNA)",
            "Complemento sérico (C3, C4, CH50)",
            "Hemograma completo",
            "Urinálise com proteinúria de 24h",
            "Anti-Smith, Anti-Ro, Anti-La",
            "Anticorpos antifosfolipídeos",
        ],
        "especialistas": [
            "Reumatologista",
            "Nefrologista (quando há envolvimento renal)",
            "Dermatologista",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "prioritária", "Muito Alto": "urgente",
        },
        "nota_clinica": "LES afeta predominantemente mulheres em idade fértil. Fotoproteção e monitoramento renal são pilares do acompanhamento.",
    },

    "artrite_reumatoide": {
        "exames": [
            "Fator Reumatoide (FR)",
            "Anti-CCP (anticorpo anti-peptídeo citrulinado)",
            "PCR e VHS (inflamação)",
            "Hemograma completo",
            "Radiografia de mãos e pés",
            "Ultrassonografia articular",
        ],
        "especialistas": [
            "Reumatologista",
            "Fisioterapeuta especializado em reumatologia",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "prioritária", "Muito Alto": "urgente",
        },
        "nota_clinica": "Diagnóstico e tratamento precoces previnem dano articular irreversível. Anti-CCP é altamente específico.",
    },

    "diabetes_tipo1": {
        "exames": [
            "Glicemia de jejum e HbA1c",
            "Autoanticorpos (anti-GAD, anti-IA2, anti-insulina, anti-ZnT8)",
            "Peptídeo C",
            "Tipagem HLA (DR3, DR4)",
            "Urinálise e microalbuminúria",
        ],
        "especialistas": [
            "Endocrinologista",
            "Diabetologista",
            "Nutricionista especializado em diabetes",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "prioritária", "Muito Alto": "urgente",
        },
        "nota_clinica": "Triagem de autoanticorpos recomendada em familiares de 1º grau. Programas de prevenção podem retardar o início.",
    },

    "esclerose_multipla": {
        "exames": [
            "Ressonância Magnética de crânio e medula espinhal (com e sem contraste)",
            "Potenciais evocados visuais, auditivos e somatossensitivos",
            "Análise do líquido cefalorraquidiano (bandas oligoclonais)",
            "Fundo de olho",
            "Tipagem HLA",
        ],
        "especialistas": [
            "Neurologista especializado em doenças desmielinizantes",
            "Oftalmologista",
            "Fisioterapeuta neurológico",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "prioritária", "Muito Alto": "urgente",
        },
        "nota_clinica": "Diagnóstico conforme critérios de McDonald. Início precoce de terapia modificadora de doença reduz surtos e progressão.",
    },

    "doenca_celica": {
        "exames": [
            "IgA anti-transglutaminase tecidual (anti-tTG)",
            "IgA anti-endomísio (EMA)",
            "IgA sérica total (excluir deficiência de IgA)",
            "Biópsia duodenal por endoscopia (padrão-ouro)",
            "Tipagem HLA DQ2/DQ8",
            "Hemograma (anemia ferropriva)",
        ],
        "especialistas": [
            "Gastroenterologista",
            "Nutricionista especializado",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "prioritária", "Muito Alto": "urgente",
        },
        "nota_clinica": "Dieta isenta de glúten é o único tratamento. Triagem de familiares de 1º grau é recomendada.",
    },

    "hashimoto": {
        "exames": [
            "TSH ultrassensível",
            "T4 livre e T3 livre",
            "Anti-TPO (anticorpo antiperoxidase tireoidiana)",
            "Anti-Tireoglobulina",
            "Ultrassonografia de tireoide",
        ],
        "especialistas": [
            "Endocrinologista",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "eletiva", "Alto": "prioritária", "Muito Alto": "prioritária",
        },
        "nota_clinica": "Monitoramento semestral de TSH. Levotiroxina indicada quando há hipotireoidismo clínico ou subclínico sintomático.",
    },

    "doenca_graves": {
        "exames": [
            "TSH, T4 livre, T3 total",
            "TRAb (anticorpo anti-receptor de TSH)",
            "Anti-TPO",
            "Ultrassonografia com Doppler de tireoide",
            "Cintilografia de tireoide",
        ],
        "especialistas": [
            "Endocrinologista",
            "Oftalmologista (oftalmopatia de Graves)",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "prioritária", "Muito Alto": "urgente",
        },
        "nota_clinica": "Hipertireoidismo autoimune. Crise tireotóxica é emergência médica. Monitoramento cardíaco em pacientes idosos.",
    },

    "psoríase": {
        "exames": [
            "Avaliação clínica e dermatológica",
            "Biópsia de pele (quando diagnóstico duvidoso)",
            "Perfil lipídico (síndrome metabólica associada)",
            "Glicemia de jejum",
            "PCR e VHS",
            "Radiografia de articulações (artrite psoriásica)",
        ],
        "especialistas": [
            "Dermatologista",
            "Reumatologista (artrite psoriásica)",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "eletiva", "Alto": "prioritária", "Muito Alto": "prioritária",
        },
        "nota_clinica": "Psoríase grave associa-se a maior risco cardiovascular e metabólico. Acompanhamento dermatológico regular.",
    },

    "espondilite_anquilosante": {
        "exames": [
            "HLA-B27 (tipagem)",
            "PCR e VHS",
            "Radiografia de pelve e coluna lombar (articulações sacroilíacas)",
            "Ressonância Magnética de sacroilíacas",
            "Hemograma completo",
        ],
        "especialistas": [
            "Reumatologista",
            "Fisioterapeuta / Especialista em reabilitação",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "prioritária", "Muito Alto": "urgente",
        },
        "nota_clinica": "Diagnóstico precoce e fisioterapia regular reduzem progressão da anquilose. HLA-B27 positivo em ~90% dos casos.",
    },

    "doenca_crohn": {
        "exames": [
            "Colonoscopia com biópsia (ileocolonoscopia)",
            "Calprotectina fecal",
            "PCR e VHS",
            "Hemograma e ferritina (anemia)",
            "Enterografia por RM (intestino delgado)",
            "ANCA e ASCA (diagnóstico diferencial)",
        ],
        "especialistas": [
            "Gastroenterologista especializado em DII",
            "Nutricionista especializado",
            "Proctologista (complicações perianais)",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "prioritária", "Muito Alto": "urgente",
        },
        "nota_clinica": "Doença inflamatória intestinal crônica com padrão transmural. Pode afetar qualquer segmento do trato gastrointestinal.",
    },

    "colite_ulcerativa": {
        "exames": [
            "Colonoscopia com biópsia",
            "Calprotectina fecal",
            "PCR e VHS",
            "Hemograma completo",
            "pANCA (diagnóstico diferencial)",
            "Cultura de fezes (excluir infecção)",
        ],
        "especialistas": [
            "Gastroenterologista especializado em DII",
            "Nutricionista especializado",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "prioritária", "Muito Alto": "urgente",
        },
        "nota_clinica": "Maior risco de câncer colorretal após 8-10 anos de doença extensa. Colonoscopia de vigilância a cada 1-2 anos.",
    },

    "miastenia_gravis": {
        "exames": [
            "Anticorpos anti-AChR (receptor de acetilcolina)",
            "Anticorpos anti-MuSK",
            "Eletroneuromiografia (ENMG)",
            "Teste do edrofônio (Tensilon)",
            "TC ou RM de mediastino (timoma)",
            "Função respiratória (espirometria)",
        ],
        "especialistas": [
            "Neurologista",
            "Cirurgião torácico (timectomia)",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Crise miastênica (insuficiência respiratória) é emergência. Timectomia recomendada para pacientes jovens com timoma.",
    },

    "sindrome_sjogren": {
        "exames": [
            "Anti-Ro/SSA e Anti-La/SSB",
            "FAN",
            "Biópsia de glândula salivar menor",
            "Teste de Schirmer (olho seco)",
            "Eletroforese de proteínas (hipergamaglobulinemia)",
            "Urinálise (envolvimento renal)",
        ],
        "especialistas": [
            "Reumatologista",
            "Oftalmologista",
            "Otorrinolaringologista",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "eletiva", "Alto": "prioritária", "Muito Alto": "prioritária",
        },
        "nota_clinica": "Associado a maior risco de linfoma não-Hodgkin. Vigilância regular recomendada.",
    },

    "vitiligo": {
        "exames": [
            "Avaliação clínica com lâmpada de Wood",
            "TSH (associação com tireoidite)",
            "Anti-TPO e Anti-Tireoglobulina",
            "FAN (excluir LES associado)",
            "Glicemia de jejum (DM1 associado)",
        ],
        "especialistas": [
            "Dermatologista",
            "Endocrinologista (doenças tireoidianas associadas)",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "eletiva", "Alto": "eletiva", "Muito Alto": "prioritária",
        },
        "nota_clinica": "Condição autoimune benigna. Fotoproteção solar rigorosa. Vigilância de outras doenças autoimunes associadas.",
    },

    "alopecia_areata": {
        "exames": [
            "Avaliação clínica e tricoscopia",
            "TSH e hormônios tireoidianos",
            "FAN, Anti-TPO",
            "Hemograma e ferritina (anemia ferropriva)",
            "Biópsia de couro cabeludo (casos duvidosos)",
        ],
        "especialistas": [
            "Dermatologista especializado em tricologia",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "eletiva", "Alto": "eletiva", "Muito Alto": "prioritária",
        },
        "nota_clinica": "Doença autoimune com perda de cabelo reversível na maioria dos casos. Monitoramento de outras autoimunidades.",
    },

    # ================================================================
    # DOENÇAS GENÉTICAS RARAS
    # ================================================================

    "huntington": {
        "exames": [
            "Teste genético HTT (número de repetições CAG) — diagnóstico definitivo",
            "Neuroimagem (RM de crânio — atrofia do núcleo caudado)",
            "Avaliação neuropsicológica formal",
            "Eletroencefalograma",
            "Avaliação oftalmológica (movimentos sacádicos)",
        ],
        "especialistas": [
            "Neurologista especializado em doenças do movimento",
            "Geneticista clínico / Oncogeneticista",
            "Psiquiatra (componente comportamental)",
            "Neuropsicologa",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "O teste preditivo deve ser precedido de aconselhamento genético especializado. Não há cura; tratamento é paliativo e multidisciplinar.",
    },

    "neurofibromatose": {
        "exames": [
            "Teste genético NF1",
            "Avaliação oftalmológica (nódulos de Lisch, glioma óptico)",
            "Ressonância Magnética de crânio e medula",
            "Avaliação dermatológica (manchas café-com-leite, neurofibromas)",
            "Raios-X de ossos (displasias ósseas)",
            "Ecocardiograma (estenose pulmonar)",
        ],
        "especialistas": [
            "Neurologista",
            "Geneticista clínico",
            "Dermatologista",
            "Oftalmologista",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "prioritária", "Muito Alto": "urgente",
        },
        "nota_clinica": "Doença multissistêmica com manifestações progressivas. Vigilância anual multidisciplinar recomendada.",
    },

    "fibrose_cistica": {
        "exames": [
            "Teste do suor (cloreto de sódio > 60 mEq/L — diagnóstico)",
            "Teste genético CFTR (painel de mutações)",
            "Prova de função pulmonar (espirometria)",
            "Tomografia de tórax de alta resolução",
            "Elastase fecal-1 (insuficiência pancreática exócrina)",
            "Cultura de escarro (Pseudomonas, Staphylococcus)",
            "Glicemia e HbA1c (DRFC — diabetes)",
        ],
        "especialistas": [
            "Pneumologista especializado em fibrose cística",
            "Geneticista clínico",
            "Gastroenterologista / Hepatologista",
            "Nutricionista especializado",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "prioritária",
            "Moderado": "urgente", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Doença sistêmica grave. Diagnóstico precoce via triagem neonatal e início imediato de fisioterapia respiratória e suporte nutricional são essenciais.",
    },

    "anemia_falciforme": {
        "exames": [
            "Hemograma completo com reticulócitos",
            "Eletroforese de hemoglobina (padrão-ouro)",
            "Teste de Falcização (células em foice)",
            "HPLC (cromatografia líquida de alta eficiência)",
            "Bilirrubinas (hiperbilirrubinemia indireta)",
            "LDH e haptoglobina (hemólise)",
            "Ultrassonografia abdominal (baço, cálculos biliares)",
        ],
        "especialistas": [
            "Hematologista",
            "Geneticista clínico",
            "Pediatra especializado (crianças)",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "prioritária",
            "Moderado": "urgente", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Triagem neonatal obrigatória no Brasil (teste do pezinho). Crises vaso-oclusivas são emergências. Profilaxia com penicilina até os 5 anos.",
    },

    "fenilcetonuria": {
        "exames": [
            "Fenilalanina plasmática (padrão-ouro)",
            "Teste do pezinho ampliado (triagem neonatal)",
            "Teste genético PAH",
            "BH4 (neopterina e biopterina em urina — diferenciar variantes)",
            "Neuroimagem (RM de crânio em casos tardios)",
        ],
        "especialistas": [
            "Geneticista clínico / Especialista em erros inatos do metabolismo",
            "Neuropediatra",
            "Nutricionista especializado",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "prioritária",
            "Moderado": "urgente", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Diagnóstico e dieta restrita em fenilalanina desde o nascimento previnem deficiência intelectual. Mulheres em idade fértil necessitam controle rigoroso.",
    },

    "hemofilia_a": {
        "exames": [
            "TTPA (tempo de tromboplastina parcial ativada) — prolongado",
            "Dosagem de Fator VIII (diagnóstico definitivo)",
            "Teste genético F8",
            "Inibidores de Fator VIII (pesquisa de inibidores)",
            "Hemograma completo",
        ],
        "especialistas": [
            "Hematologista especializado em coagulopatias",
            "Geneticista clínico",
            "Ortopedista (hemartroses)",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "prioritária",
            "Moderado": "urgente", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Centros de tratamento de hemofilia (CTH) são referência. Infusões profiláticas de fator VIII reduzem hemartroses e sequelas articulares.",
    },

    "hemofilia_b": {
        "exames": [
            "TTPA prolongado",
            "Dosagem de Fator IX",
            "Teste genético F9",
            "Pesquisa de inibidores de Fator IX",
            "Hemograma completo",
        ],
        "especialistas": [
            "Hematologista especializado em coagulopatias",
            "Geneticista clínico",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "prioritária",
            "Moderado": "urgente", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Semelhante à Hemofilia A, mas menos frequente. Terapia gênica em desenvolvimento com resultados promissores.",
    },

    "duchenne": {
        "exames": [
            "CPK (creatinoquinase) sérica — muito elevada",
            "Teste genético DMD (deleções, duplicações, mutações de ponto)",
            "Biópsia muscular com imunohistoquímica (distrofina)",
            "Eletroneuromiografia",
            "Ecocardiograma (cardiomiopatia)",
            "Prova de função pulmonar",
        ],
        "especialistas": [
            "Neurologista / Neuropediatra",
            "Geneticista clínico",
            "Fisioterapeuta especializado",
            "Cardiologista (cardiomiopatia)",
            "Pneumologista",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "prioritária",
            "Moderado": "urgente", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Corticoesteroides (deflazacorte/prednisona) são padrão de cuidado. Ataluren indicado para mutações nonsense. Acompanhamento multidisciplinar intensivo.",
    },

    "marfan": {
        "exames": [
            "Ecocardiograma transtorácico (dilatação aórtica — anual)",
            "Angiografia/Angiotomografia de aorta",
            "Teste genético FBN1",
            "Avaliação oftalmológica (ectopia de cristalino)",
            "Radiografia de coluna (escoliose)",
            "Avaliação ortopédica",
        ],
        "especialistas": [
            "Cardiologista / Cirurgião cardiovascular",
            "Geneticista clínico",
            "Oftalmologista",
            "Ortopedista",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Dissecção/ruptura de aorta é a principal causa de morte. Betabloqueadores ou losartana para retardar dilatação. Evitar esportes de contato e esforço intenso.",
    },

    "ehlers_danlos": {
        "exames": [
            "Teste genético (COL5A1, COL5A2 — tipo clássico; COL3A1 — tipo vascular)",
            "Avaliação clínica da hipermobilidade articular (Escore de Beighton)",
            "Ecocardiograma (tipo vascular)",
            "Angiotomografia de aorta (tipo vascular)",
            "Biópsia de pele com microscopia eletrônica",
        ],
        "especialistas": [
            "Geneticista clínico",
            "Reumatologista",
            "Cardiologista (tipo vascular)",
            "Fisioterapeuta especializado em hipermobilidade",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "O tipo vascular (EDS-IV) é o mais grave, com risco de ruptura arterial/visceral espontânea. Vigilância vascular intensiva.",
    },

    "doenca_wilson": {
        "exames": [
            "Ceruloplasmina sérica (baixa em 85% dos casos)",
            "Cobre sérico e cobre urinário de 24h",
            "Cobre hepático (biópsia de fígado)",
            "Fenda de Kayser-Fleischer (lâmpada de fenda)",
            "Teste genético ATP7B",
            "Transaminases e função hepática",
            "Ressonância Magnética de crânio (manifestações neurológicas)",
        ],
        "especialistas": [
            "Hepatologista",
            "Neurologista",
            "Geneticista clínico",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Doença tratável se diagnosticada a tempo. D-penicilamina ou zinco são tratamentos de primeira linha. Triagem obrigatória de irmãos.",
    },

    "gaucher": {
        "exames": [
            "Atividade da beta-glicocerebrosidase em leucócitos (diagnóstico definitivo)",
            "Teste genético GBA",
            "Quitotriosidase plasmática (marcador de atividade)",
            "Hemograma (anemia, trombocitopenia)",
            "RM de fígado, baço e medula óssea",
            "Densitometria óssea",
        ],
        "especialistas": [
            "Geneticista clínico / Especialista em erros inatos do metabolismo",
            "Hematologista",
            "Hepatologista",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Terapia de reposição enzimática (imiglicerase) é altamente eficaz. Diagnóstico precoce previne complicações ósseas graves.",
    },

    "tay_sachs": {
        "exames": [
            "Atividade de Hexosaminidase A em leucócitos ou plasma",
            "Teste genético HEXA",
            "Fundoscopia (mancha vermelho-cereja)",
            "Eletroencefalograma",
            "Ressonância Magnética de crânio",
        ],
        "especialistas": [
            "Neurologista / Neuropediatra",
            "Geneticista clínico",
            "Oftalmologista",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "prioritária",
            "Moderado": "urgente", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Doença fatal sem tratamento curativo. Triagem de portadores em populações de alto risco (judeus Ashkenazi). Diagnóstico pré-natal disponível.",
    },

    "talassemia": {
        "exames": [
            "Hemograma completo (anemia microcítica hipocrômica grave)",
            "Eletroforese de hemoglobina (HbF elevada, HbA ausente ou reduzida)",
            "HPLC",
            "Teste genético HBB",
            "Ferritina e saturação de transferrina (sobrecarga de ferro)",
            "Ecocardiograma (cardiomiopatia por ferro)",
        ],
        "especialistas": [
            "Hematologista",
            "Geneticista clínico",
            "Cardiologista (sobrecarga de ferro)",
            "Endocrinologista (hipogonadismo, diabetes)",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "prioritária",
            "Moderado": "urgente", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Transfusões regulares e quelação de ferro são padrão de cuidado. Transplante de medula óssea é o único tratamento curativo.",
    },

    "ataxia_friedreich": {
        "exames": [
            "Teste genético FXN (expansão de repetição GAA)",
            "Eletroneuromiografia (neuropatia sensorial)",
            "Ecocardiograma (cardiomiopatia hipertrófica)",
            "Ressonância Magnética de crânio e medula",
            "Glicemia e HbA1c (diabetes associado)",
            "ECG",
        ],
        "especialistas": [
            "Neurologista especializado em ataxias hereditárias",
            "Cardiologista",
            "Geneticista clínico",
            "Fisioterapeuta / Fonoaudiólogo",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "A cardiomiopatia é a principal causa de morte. Monitoramento cardiológico semestral obrigatório.",
    },

    "esclerose_tuberosa": {
        "exames": [
            "Teste genético TSC1/TSC2",
            "Ressonância Magnética de crânio (tubers corticais, nodules subependimários)",
            "TC de tórax (linfangioleiomiomatose — mulheres)",
            "TC ou RM de abdômen (angiomiolipomas renais)",
            "Ecocardiograma (rabdomiomas cardíacos)",
            "Fundoscopia (hamartomas retinianos)",
            "Eletroencefalograma (epilepsia)",
        ],
        "especialistas": [
            "Neurologista",
            "Geneticista clínico",
            "Nefrologista",
            "Dermatologista",
            "Pneumologista (LAM)",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Doença multissistêmica. Inibidores mTOR (everolimo, sirolimo) são tratamento específico. Epilepsia é manifestação mais comum.",
    },

    "osteogenese_imperfeita": {
        "exames": [
            "Teste genético COL1A1/COL1A2 (e outros conforme tipo)",
            "Densitometria óssea (DEXA)",
            "Radiografia de esqueleto completo",
            "Dosagem de fosfatase alcalina",
            "Audiometria (perda auditiva progressiva)",
        ],
        "especialistas": [
            "Ortopedista especializado em doenças ósseas raras",
            "Geneticista clínico",
            "Endocrinologista (metabolismo mineral)",
            "Otorrinolaringologista (deficiência auditiva)",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Bifosfonatos (pamidronato, zoledronato) melhoram densidade óssea. Reabilitação e prevenção de fraturas são prioridades.",
    },

    "atrofia_muscular_espinhal": {
        "exames": [
            "Teste genético SMN1 (deleção homozigótica — diagnóstico definitivo)",
            "Eletroneuromiografia",
            "CPK sérica",
            "Biópsia muscular (quando necessário)",
            "Prova de função pulmonar",
            "Avaliação de deglutição",
        ],
        "especialistas": [
            "Neurologista / Neuropediatra",
            "Geneticista clínico",
            "Pneumologista",
            "Fisioterapeuta / Fonoaudiólogo",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "prioritária",
            "Moderado": "urgente", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Tratamentos aprovados: nusinersen (intratecal), onasemnogene abeparvovec (terapia gênica), risdiplam (oral). Início precoce é crítico para desfechos.",
    },

    "sindrome_angelman": {
        "exames": [
            "Análise de metilação do cromossomo 15 (SNRPN)",
            "Microarray cromossômico (CGH-array)",
            "Sequenciamento de UBE3A",
            "Eletroencefalograma (padrão característico)",
            "Ressonância Magnética de crânio",
        ],
        "especialistas": [
            "Neuropediatra",
            "Geneticista clínico",
            "Fonoaudiólogo",
            "Terapeuta ocupacional",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Diagnóstico precoce e intervenção terapêutica intensiva melhoram qualidade de vida e desenvolvimento. Sem cura disponível.",
    },

    # ================================================================
    # CARDIOVASCULARES
    # ================================================================

    "cardiomiopatia_hipertrofica": {
        "exames": [
            "Ecocardiograma transtorácico (espessura de septo > 15mm)",
            "Holter 24h e 48h (arritmias)",
            "Teste de esforço com análise de pressão",
            "RM cardíaca com gadolínio (fibrose miocárdica)",
            "Teste genético (MYH7, MYBPC3, TNNT2, TNNI3)",
            "ECG (critérios de voltagem e repolarização)",
        ],
        "especialistas": [
            "Cardiologista especializado em cardiomiopatias",
            "Arritmologista",
            "Geneticista clínico",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Principal causa de morte súbita em jovens atletas. CDI profilático indicado em pacientes de alto risco. Triagem de familiares de 1º grau.",
    },

    "cardiomiopatia_dilatada": {
        "exames": [
            "Ecocardiograma (FE < 50%, dilatação ventricular)",
            "RM cardíaca",
            "Holter 24h",
            "Teste genético (LMNA, MYH7, SCN5A, TTN)",
            "BNP / NT-proBNP (insuficiência cardíaca)",
            "Biópsia miocárdica (casos selecionados)",
        ],
        "especialistas": [
            "Cardiologista especializado em insuficiência cardíaca",
            "Geneticista clínico",
            "Eletrofisiologista (LMNA — alto risco de bloqueio/MS)",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Mutações em LMNA têm pior prognóstico e risco elevado de morte súbita. CDI deve ser considerado precocemente.",
    },

    "hipercolesterolemia_familiar": {
        "exames": [
            "Perfil lipídico completo (LDL > 190 mg/dL em adultos)",
            "Teste genético LDLR, APOB, PCSK9",
            "Escore clínico de Dutch Lipid Clinic (diagnóstico)",
            "Ultrassonografia de carótidas (espessura íntima-média)",
            "Tomografia de coronárias com escore de cálcio",
            "Lp(a) plasmática",
        ],
        "especialistas": [
            "Cardiologista / Clínico especializado em dislipidemia",
            "Geneticista clínico",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Início de estatina potente na infância em homozigotos. Aférese de LDL e inibidores de PCSK9 para casos graves.",
    },

    "sindrome_brugada": {
        "exames": [
            "ECG (padrão tipo 1 — elevação de ST côncava em V1-V2)",
            "Teste de provocação com ajmalina ou flecainida",
            "Holter 24h",
            "Teste genético SCN5A",
            "Estudo eletrofisiológico (casos selecionados)",
        ],
        "especialistas": [
            "Cardiologista / Eletrofisiologista",
            "Geneticista clínico",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "CDI é o único tratamento comprovado para prevenir morte súbita. Evitar febre alta, medicamentos que bloqueiam canal de sódio e hipocalemia.",
    },

    "displasia_arritmogenica_vd": {
        "exames": [
            "RM cardíaca (substituição fibrogordurosa — critério diagnóstico)",
            "ECG (onda épsilon, bloqueio de ramo direito)",
            "Holter 24h",
            "Ecocardiograma",
            "Teste genético (PKP2, DSP, DSG2, DSC2, JUP)",
            "Angiografia de VD (casos selecionados)",
        ],
        "especialistas": [
            "Cardiologista especializado em cardiomiopatias / Arritmologista",
            "Geneticista clínico",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Atividade física intensa acelera progressão da doença. Restrição esportiva obrigatória. CDI indicado em pacientes com taquicardia ventricular sustentada.",
    },

    "aneurisma_aorta_familiar": {
        "exames": [
            "Angiotomografia ou Angioressonância de aorta torácica",
            "Ecocardiograma transtorácico",
            "Teste genético (ACTA2, MYH11, SMAD3, TGFBR1/2, FBN1)",
            "Ultrassonografia de aorta abdominal",
        ],
        "especialistas": [
            "Cirurgião cardiovascular / Angiovascular",
            "Cardiologista",
            "Geneticista clínico",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Cirurgia profilática indicada quando diâmetro > 5cm (ou 4,5cm em mutações de alto risco). Betabloqueadores e losartana retardam dilatação.",
    },

    # ================================================================
    # NEUROLÓGICAS
    # ================================================================

    "alzheimer_familiar": {
        "exames": [
            "Teste genético PSEN1, PSEN2, APP (início precoce)",
            "Apoliproteína E (APOE ε4) — fator de risco (não diagnóstico)",
            "Neuroimagem: RM de crânio (atrofia hipocampal)",
            "PET-scan de amiloide (quando disponível)",
            "Biomarcadores em LCR (Aβ42, tau total, tau fosforilada)",
            "Avaliação neuropsicológica completa",
        ],
        "especialistas": [
            "Neurologista especializado em demências",
            "Geneticista clínico",
            "Geriatra",
            "Neuropsicólogo",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Teste preditivo deve ser precedido de aconselhamento genético rigoroso. Novos anticorpos anti-amiloide (lecanemab, donanemab) para fases iniciais.",
    },

    "parkinson_familiar": {
        "exames": [
            "Teste genético LRRK2, SNCA, PARK2, PINK1, DJ-1",
            "DaTscan (SPECT com ioflupano — neuroimagem dopaminérgica)",
            "Avaliação neurológica com escalas (UPDRS, H&Y)",
            "Olfatometria (hiposmia precoce)",
            "RM de crânio (excluir outras causas)",
            "Polissonografia (distúrbio comportamental do sono REM)",
        ],
        "especialistas": [
            "Neurologista especializado em distúrbios do movimento",
            "Geneticista clínico",
            "Fisioterapeuta / Fonoaudiólogo",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "prioritária", "Muito Alto": "urgente",
        },
        "nota_clinica": "Levodopa/carbidopa permanece tratamento principal. Estimulação cerebral profunda (DBS) para casos avançados. Exercício regular tem benefício neuroprotetor.",
    },

    "ela_familiar": {
        "exames": [
            "Teste genético SOD1, C9orf72, FUS, TARDBP",
            "Eletroneuromiografia (ENMG) — critérios diagnósticos de El Escorial",
            "Ressonância Magnética de crânio e medula",
            "Prova de função pulmonar seriada",
            "Avaliação de deglutição",
        ],
        "especialistas": [
            "Neurologista especializado em doenças do neurônio motor",
            "Geneticista clínico",
            "Pneumologista (VNI)",
            "Nutricionista / Fonoaudiólogo",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Riluzol e edaravone têm benefício modesto. Cuidados paliativos precoces e multidisciplinares são essenciais. Ventilação não invasiva prolonga sobrevida.",
    },

    "epilepsia_genetica": {
        "exames": [
            "Eletroencefalograma (EEG) de vigília e sono",
            "Vídeo-EEG (classificação das crises)",
            "Ressonância Magnética de crânio de alta resolução",
            "Painel genético de epilepsias (SCN1A, SCN2A, KCNQ2, CDKL5, etc.)",
            "Metabólico: aminoácidos plasmáticos, ácidos orgânicos urinários",
        ],
        "especialistas": [
            "Neurologista / Neuropediatra especializado em epilepsia",
            "Geneticista clínico",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Identificação da causa genética orienta a escolha do antiepiléptico. SCN1A+ (Síndrome de Dravet): evitar carbamazepina e lamotrigina.",
    },

    "charcot_marie_tooth": {
        "exames": [
            "Eletroneuromiografia (velocidade de condução)",
            "Teste genético PMP22, MPZ, GJB1, MFN2 (painel CMT)",
            "Biópsia de nervo sural (casos selecionados)",
            "Avaliação ortopédica (pé cavo, escoliose)",
        ],
        "especialistas": [
            "Neurologista especializado em neuropatias",
            "Geneticista clínico",
            "Ortopedista",
            "Fisioterapeuta",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "prioritária", "Muito Alto": "urgente",
        },
        "nota_clinica": "Não há tratamento curativo. Fisioterapia regular, órteses e cirurgia ortopédica melhoram funcionalidade. Progressão lenta na maioria dos casos.",
    },

    # ================================================================
    # METABÓLICAS
    # ================================================================

    "diabetes_tipo2_genetico": {
        "exames": [
            "Glicemia de jejum e HbA1c",
            "Teste oral de tolerância à glicose (TOTG)",
            "Insulinemia de jejum e HOMA-IR",
            "Perfil lipídico completo",
            "Microalbuminúria e função renal (creatinina, TFG)",
            "Fundo de olho (retinopatia)",
        ],
        "especialistas": [
            "Endocrinologista / Diabetologista",
            "Nutricionista especializado em diabetes",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "prioritária", "Muito Alto": "urgente",
        },
        "nota_clinica": "Mudança de estilo de vida (dieta e exercício) pode prevenir ou retardar o início do DM2 mesmo com forte predisposição genética.",
    },

    "diabetes_mody": {
        "exames": [
            "Glicemia de jejum",
            "Peptídeo C (preservado)",
            "Autoanticorpos pancreáticos (negativos)",
            "Teste genético: painel MODY (GCK, HNF1A, HNF4A, HNF1B, etc.)",
            "Urinálise e função renal (MODY 5 — HNF1B: rim policístico)",
        ],
        "especialistas": [
            "Endocrinologista com experiência em MODY",
            "Geneticista clínico",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "prioritária", "Muito Alto": "urgente",
        },
        "nota_clinica": "MODY-GCK: hipoglicemia leve sem complicações, geralmente não requer tratamento. MODY-HNF1A e HNF4A: respondem a sulfonilureias. Diagnóstico genético muda o tratamento.",
    },

    "hemocromatose": {
        "exames": [
            "Ferritina sérica e saturação de transferrina",
            "Teste genético HFE (C282Y, H63D)",
            "Biópsia hepática com quantificação de ferro (casos selecionados)",
            "Ressonância Magnética de fígado (mensuração de ferro)",
            "Transaminases e função hepática",
            "Glicemia (diabetes secundário)",
            "Testosterona / FSH / LH (hipogonadismo)",
        ],
        "especialistas": [
            "Hepatologista",
            "Geneticista clínico",
            "Endocrinologista (complicações hormonais)",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "prioritária", "Muito Alto": "urgente",
        },
        "nota_clinica": "Flebotomia seriada (sangrias) é o tratamento principal e altamente eficaz quando iniciada antes da cirrose. Triagem familiar obrigatória.",
    },

    "deficiencia_alfa1_antitripsina": {
        "exames": [
            "Dosagem de alfa-1 antitripsina sérica",
            "Fenótipo Pi (por focalização isoelétrica — Pi ZZ, Pi SZ)",
            "Teste genético SERPINA1",
            "Prova de função pulmonar (enfisema de início precoce)",
            "TC de tórax (distribuição panlobular — bases)",
            "Transaminases e biópsia hepática (doença hepática)",
        ],
        "especialistas": [
            "Pneumologista",
            "Hepatologista",
            "Geneticista clínico",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Cessação do tabagismo é a intervenção mais importante. Terapia de reposição com alfa-1 antitripsina para casos pulmonares graves.",
    },

    "galactosemia": {
        "exames": [
            "Teste do pezinho (triagem neonatal — galactose total)",
            "Atividade de galactose-1-fosfato uridiltransferase em eritrócitos",
            "Galactose-1-fosfato em sangue seco",
            "Teste genético GALT",
            "Função hepática (transaminases, coagulograma)",
            "Avaliação cognitiva e neurológica",
        ],
        "especialistas": [
            "Geneticista clínico / Especialista em erros inatos do metabolismo",
            "Hepatologista",
            "Neuropediatra",
            "Nutricionista especializado",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "prioritária",
            "Moderado": "urgente", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Retirada imediata de lactose/galactose da dieta é vital no período neonatal. Mesmo tratado, risco de complicações a longo prazo (cognitivas, ovarianas).",
    },

    "porfiria_aguda": {
        "exames": [
            "Porfobilinogênio urinário (PBG) — durante crise",
            "Ácido delta-aminolevulínico (ALA) urinário",
            "Mutação genética HMBS",
            "Dosagem de porfirinas em urina, fezes e plasma",
            "Eletrólitos (hiponatremia durante crise)",
        ],
        "especialistas": [
            "Hematologista / Especialista em porfirias",
            "Hepatologista",
            "Geneticista clínico",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Crise aguda é emergência médica: hemina IV (Normosang). Evitar fármacos desencadeantes. Givosiran (RNA de interferência) aprovado para profilaxia.",
    },

    # ================================================================
    # PSIQUIÁTRICAS
    # ================================================================

    "esquizofrenia": {
        "exames": [
            "Avaliação psiquiátrica estruturada (escalas PANSS, BPRS)",
            "Neuroimagem (RM de crânio — exclusão de causas orgânicas)",
            "Hemograma, função tireoidiana, metabólico (excluir causas orgânicas)",
            "EEG (excluir epilepsia)",
            "Painel genético (pesquisa — deleções 22q11, 15q11-q13)",
        ],
        "especialistas": [
            "Psiquiatra",
            "Neurologista (causas orgânicas)",
            "Geneticista clínico (formas familiares)",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "prioritária", "Muito Alto": "urgente",
        },
        "nota_clinica": "Intervenção precoce em psicose tem melhor prognóstico. Antipsicóticos são pilares do tratamento. Suporte familiar e reabilitação psicossocial são essenciais.",
    },

    "transtorno_bipolar": {
        "exames": [
            "Avaliação psiquiátrica estruturada",
            "Perfil tireoidiano (TSH, T4) — antes de lítio",
            "Função renal e creatinina — antes de lítio",
            "Hemograma e eletrólitos",
            "RM de crânio (exclusão de causas orgânicas)",
        ],
        "especialistas": [
            "Psiquiatra",
            "Neurologista (diagnóstico diferencial)",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "prioritária", "Muito Alto": "urgente",
        },
        "nota_clinica": "Lítio é o estabilizador de humor de referência. Monitorar litemia, função renal e tireoidiana regularmente. Psicoeducação reduz recaídas.",
    },

    "autismo_genetico": {
        "exames": [
            "Avaliação clínica e escalas (ADOS-2, ADI-R)",
            "Microarray cromossômico (CGH-array) — primeira linha",
            "Sequenciamento de exoma clínico",
            "Pesquisa de X-frágil (FMR1)",
            "Perfil metabólico (aminoácidos, orgânicos urinários)",
            "Audiometria (excluir perda auditiva)",
        ],
        "especialistas": [
            "Neuropediatra",
            "Geneticista clínico",
            "Fonoaudiólogo",
            "Terapeuta ocupacional",
            "Psicólogo especializado em TEA",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "prioritária", "Muito Alto": "urgente",
        },
        "nota_clinica": "Diagnóstico e intervenção precoces melhoram significativamente o prognóstico. Causa genética identificável em 30-40% dos casos.",
    },

    "tdah_genetico": {
        "exames": [
            "Avaliação clínica e escalas (Conners, SNAP-IV)",
            "Avaliação neuropsicológica (atenção, funções executivas)",
            "ECG (antes de metilfenidato em casos selecionados)",
            "Função tireoidiana (excluir hipertireoidismo)",
        ],
        "especialistas": [
            "Psiquiatra infantil / Neuropediatra",
            "Neuropsicólogo",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "eletiva", "Alto": "prioritária", "Muito Alto": "prioritária",
        },
        "nota_clinica": "Combinação de terapia comportamental e farmacoterapia (metilfenidato, lisdexanfetamina) tem melhor eficácia. Identificação precoce reduz impacto escolar e social.",
    },

    # ================================================================
    # DOENÇAS RARAS ADICIONAIS (NOVAS)
    # ================================================================

    "fabry": {
        "exames": [
            "Atividade de alfa-galactosidase A em leucócitos ou plasma seco",
            "Teste genético GLA",
            "Gb3 e lyso-Gb3 plasmáticos (biomarcadores)",
            "Ecocardiograma (cardiomiopatia hipertrófica)",
            "Função renal e proteinúria",
            "Ressonância Magnética de crânio (AVC prematuro)",
            "Avaliação dermatológica (angioqueratomas)",
        ],
        "especialistas": [
            "Geneticista clínico / Especialista em doenças lisossômicas",
            "Cardiologista",
            "Nefrologista",
            "Neurologista",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Terapia de reposição enzimática (agalsidase alfa ou beta) e migalastat (chaperonas) estão disponíveis. Diagnóstico precoce previne complicações renais, cardíacas e neurológicas.",
    },

    "pompe": {
        "exames": [
            "Atividade de alfa-glicosidase ácida em sangue seco (DBS) — triagem",
            "Confirmação em leucócitos ou fibroblastos",
            "Teste genético GAA",
            "CPK sérica (elevada)",
            "Prova de função pulmonar (fraqueza respiratória)",
            "Ecocardiograma (cardiomegalia — forma infantil)",
            "Biópsia muscular (glicogênio em lisossomos)",
        ],
        "especialistas": [
            "Neurologista / Especialista em doenças neuromusculares",
            "Geneticista clínico",
            "Pneumologista",
            "Fisioterapeuta",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Terapia de reposição enzimática (alglicosidase alfa; cipaglucosidase alfa) é o tratamento padrão. Forma infantil clássica é emergência neonatal.",
    },

    "mucopolissacaridose_i": {
        "exames": [
            "Glucosaminoglicanos (GAGs) urinários — triagem",
            "Atividade de alfa-L-iduronidase em leucócitos",
            "Teste genético IDUA",
            "Ressonância Magnética de crânio e medula cervical",
            "Ecocardiograma",
            "Audiometria",
            "Avaliação oftalmológica (opacidade de córnea)",
        ],
        "especialistas": [
            "Geneticista clínico / Especialista em doenças lisossômicas",
            "Neurologista",
            "Cardiologista",
            "Oftalmologista",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "prioritária",
            "Moderado": "urgente", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Forma grave (Hurler): transplante de células-tronco hematopoiéticas em < 2 anos e/ou laronidase (TRE). Diagnóstico precoce é crítico.",
    },

    "rett": {
        "exames": [
            "Teste genético MECP2 (mutação de ponto ou deleção)",
            "Eletroencefalograma",
            "Ressonância Magnética de crânio",
            "Raio-X de coluna (escoliose)",
            "Polissonografia (apneia central)",
        ],
        "especialistas": [
            "Neuropediatra",
            "Geneticista clínico",
            "Fisioterapeuta",
            "Fonoaudiólogo",
            "Cardiologista (QT prolongado)",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Afeta quase exclusivamente meninas. Trofinetida (Daybue) aprovada em 2023 para sintomas centrais. Manejo multidisciplinar intensivo.",
    },

    "noonan": {
        "exames": [
            "Teste genético (PTPN11, SOS1, RAF1, RIT1, KRAS — painel Noonan)",
            "Ecocardiograma (estenose pulmonar, cardiomiopatia hipertrófica)",
            "ECG",
            "Hemograma (trombocitopenia, coagulopatia)",
            "Audiometria",
            "Avaliação endocrinológica (criptorquidia, baixa estatura — GH)",
        ],
        "especialistas": [
            "Geneticista clínico",
            "Cardiologista pediátrico",
            "Endocrinologista pediátrico",
            "Hematologista",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Associado a risco aumentado de leucemia mielomonocítica juvenil (JMML). Vigilância hematológica regular em portadores de PTPN11.",
    },

    "prader_willi": {
        "exames": [
            "Análise de metilação do cromossomo 15 (SNRPN) — triagem",
            "FISH para deleção 15q11-q13",
            "Microsatélites (dissomia uniparental materna)",
            "Hormônios: GH, IGF-1 (deficiência de GH)",
            "Perfil metabólico (obesidade, DM2)",
            "Polissonografia (apneia obstrutiva)",
        ],
        "especialistas": [
            "Geneticista clínico",
            "Endocrinologista pediátrico",
            "Neurologista",
            "Nutricionista especializado",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Terapia com GH melhora composição corporal, estatura e desenvolvimento motor. Controle rigoroso da alimentação é fundamental para prevenir obesidade grave.",
    },

    "williams": {
        "exames": [
            "FISH para deleção 7q11.23 (ELN)",
            "Microarray cromossômico (CGH-array)",
            "Ecocardiograma (estenose aórtica supravalvar, estenose pulmonar)",
            "Função renal e ultrassonografia (malformações renais)",
            "Cálcio sérico (hipercalcemia)",
            "Avaliação neuropsicológica",
        ],
        "especialistas": [
            "Geneticista clínico",
            "Cardiologista pediátrico",
            "Neuropediatra",
            "Nefrologista",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Estenose aórtica supravalvar pode ser grave e necessitar intervenção cirúrgica. Hipercalcemia neonatal requer tratamento imediato.",
    },

    "acondroplasia": {
        "exames": [
            "Teste genético FGFR3 (mutação p.Gly380Arg em 99% dos casos)",
            "Radiografia de esqueleto completo",
            "Ressonância Magnética de crânio (hidrocefalia, estenose de forame magno)",
            "Polissonografia (apneia obstrutiva e central)",
            "Avaliação neurológica",
        ],
        "especialistas": [
            "Geneticista clínico",
            "Ortopedista especializado em displasias ósseas",
            "Neurocirurgião",
            "Neurologista",
        ],
        "urgencia_por_risco": {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        },
        "nota_clinica": "Vosoritide aprovado para aumentar estatura em crianças. Monitoramento neurológico intensivo na infância para compressão medular cervical.",
    },
}


def get_urgency_level(disease_id: str, nivel_risco: str) -> str:
    """Retorna o nível de urgência para uma doença e nível de risco."""
    if disease_id not in DISEASE_CLINICAL_INFO:
        # Fallback genérico
        fallback = {
            "Muito Baixo": "eletiva", "Baixo": "eletiva",
            "Moderado": "prioritária", "Alto": "urgente", "Muito Alto": "urgente",
        }
        return fallback.get(nivel_risco, "eletiva")
    return DISEASE_CLINICAL_INFO[disease_id]["urgencia_por_risco"].get(nivel_risco, "eletiva")


def get_urgency_description(urgency: str) -> dict:
    """Retorna descrição e cor para o nível de urgência."""
    urgency_map = {
        "eletiva": {
            "label": "Consulta Eletiva",
            "descricao": "Agende uma consulta de rotina em até 90 dias.",
            "cor": "#28a745",
            "icone": "fa-calendar-check",
        },
        "prioritária": {
            "label": "Consulta Prioritária",
            "descricao": "Consulta necessária em até 30 dias. Informe o histórico familiar ao médico.",
            "cor": "#fd7e14",
            "icone": "fa-calendar-exclamation",
        },
        "urgente": {
            "label": "Consulta Urgente",
            "descricao": "Busque atendimento especializado em até 7 dias. Leve todos os documentos médicos disponíveis.",
            "cor": "#dc3545",
            "icone": "fa-hospital-user",
        },
    }
    return urgency_map.get(urgency, urgency_map["eletiva"])
