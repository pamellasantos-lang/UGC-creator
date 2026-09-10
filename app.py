import streamlit as st

# 1. Configuração da página em Modo Wide
st.set_page_config(
    page_title="UGC Ad Studio - Gerador Modular",
    page_icon="🎬",
    layout="wide"
)

# 2. Estilização CSS de Alta Visibilidade e Contraste
st.markdown("""
    <style>
    .stApp {
        background-color: #F8FAFC;
        color: #0F172A;
    }
    label, p, h1, h2, h3, h4, span, div {
        color: #0F172A !important;
        font-weight: 600 !important;
    }
    .stTextInput input, .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border: 2px solid #CBD5E1 !important;
        border-radius: 8px !important;
        font-size: 14px !important;
    }
    .stSelectbox div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        border: 2px solid #CBD5E1 !important;
        border-radius: 8px !important;
    }
    div[data-baseweb="popover"], div[data-baseweb="menu"], ul[role="listbox"] {
        background-color: #FFFFFF !important;
        border: 1px solid #CBD5E1 !important;
    }
    li[role="option"], div[data-baseweb="option"] {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        font-weight: 600 !important;
    }
    li[role="option"]:hover, div[data-baseweb="option"]:hover {
        background-color: #E2E8F0 !important;
        color: #0284C7 !important;
    }
    .stTextInput input::placeholder, .stTextArea textarea::placeholder {
        color: #64748B !important;
        opacity: 1 !important;
        font-weight: 400 !important;
    }
    div[data-testid="stCodeBlock"] pre {
        background-color: #0F172A !important;
        border: 2px solid #1E293B !important;
        border-radius: 10px !important;
    }
    div[data-testid="stCodeBlock"] code {
        color: #38BDF8 !important;
        font-family: 'Fira Code', 'Courier New', monospace !important;
        font-size: 13px !important;
        line-height: 1.5 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho
st.title("🎬 UGC Ad Studio - Gerador Modular")
st.caption("Crie prompts unificados em português para vídeos silenciosos, unboxing, dancinhas virais e provador no espelho.")

st.markdown("---")

col_left, col_mid, col_right = st.columns([1, 1.1, 1.2], gap="medium")

# ==========================================
# COLUNA 1: FORMATO, TIPO DE MÍDIA E DURAÇÃO
# ==========================================
with col_left:
    st.subheader("🎯 Mídia & Tempo")

    tipo_midia = st.selectbox(
        "Formato do Prompt Desejado:",
        [
            "Gerar Vídeo Direto (Com movimento e ação)",
            "Gerar Foto / Imagem Base (Para animar posteriormente)"
        ],
        help="(i) Escolha 'Vídeo' para comandos de animação ou 'Foto' para criar a imagem estática de referência."
    )

    ritmo_duracao = st.selectbox(
        "Ritmo & Duração da Câmera:",
        [
            "Câmera Lenta / Movimentos Lentos (Ideal para mostrar detalhes)",
            "Movimento Suave Padrão (Cadenciado)",
            "Dinâmico / Rápido"
        ],
        help="(i) 'Câmera Lenta' força a IA a fazer movimentos ultra-suaves, fazendo o vídeo parecer mais longo e detalhado."
    )

    tipo_plano = st.selectbox(
        "Perspectiva / Estilo da Câmera:",
        [
            "Transição POV Cama ➔ Provador no Espelho (Roupa na Cama + Modelo no Espelho)",
            "Dancinha Viral TikTok (Modelo vestindo a roupa + Coreografia de referência)",
            "Showcase de Sapato - Unboxing da Caixa ➔ Teste no Pé (POV + Espelho)",
            "Showcase Múltiplas Cores - Troca Rápida de Cores da Mesma Peça",
            "Visão POV (Apenas Mãos em Primeira Pessoa - Roupa na Cama)",
            "Showcase Model - Câmera 360° em Volta (Giro + Zooms de Detalhes da Peça)",
            "Modelo em Cena - Close-up (Rosto / Busto)",
            "Modelo em Cena - Corpo Inteiro (Lifestyle)",
            "Selfie no Espelho / Câmera Frontal"
        ],
        help="(i) Selecione o estilo de vídeo desejado."
    )

    if "Showcase Model" in tipo_plano:
        tipo_peca = st.selectbox(
            "Foco Principal do Zoom / Peça:",
            [
                "Blusa / Camiseta / Casaco (Foco na gola, estampa, textura do tecido e caimento)",
                "Bermuda / Calça / Saia (Foco nos bolsos, costuras, cintura e tecido)",
                "Tênis / Calçado (Foco no solado, acabamento, cadarço e detalhes laterais)",
                "Look Completo / Acessórios Diversos"
            ],
            help="(i) Define exatamente quais detalhes a câmera deve focar nos close-ups durante o movimento."
        )
    else:
        tipo_peca = None

    produto_nome = st.text_input(
        "Nome / Categoria do Produto:",
        placeholder="Ex: Tênis Esportivo, Pijama de Coração, Camiseta Básica...",
        help="(i) Identificação do produto para contextualizar no prompt."
    )

    if any(x in tipo_plano for x in ["Sapato", "Múltiplas Cores", "Dancinha"]):
        embalagem_efeito = False
    else:
        embalagem_efeito = st.checkbox(
            "Efeito Unboxing (Rasgar embalagem plástica antes de colocar na cama)",
            value=True,
            help="(i) Ative para incluir a ação das mãos rasgando a embalagem plástica antes de arrumar a peça na cama."
        )

    ferramenta_destino = st.selectbox(
        "Ferramenta de IA Destino:",
        [
            "Meta AI / WhatsApp AI (100% Gratuito)",
            "Google Flow / Veo (Gratuito / Acesso Grátis)",
            "Kling AI (Créditos Diários Grátis)",
            "Luma Dream Machine (Créditos Grátis)",
            "Runway Gen-3 / Hailuo AI (Testes Grátis)",
            "Flux / Midjourney (Criação de Imagem Base)"
        ]
    )

# ==========================================
# COLUNA 2: CENÁRIO E AÇÕES
# ==========================================
with col_mid:
    st.subheader("⚡ Cenário & Ações")

    cenario = st.selectbox(
        "Ambiente / Cenário:",
        [
            "Cama com edredom neutro e tapete felpudo branco",
            "Quarto moderno e iluminado com luz natural de janela",
            "Penteadeira / Banheiro de luxo com espelho",
            "Mesa minimalista de mármore",
            "Cenário urbano / Rua moderna com estética clean",
            "Fundo neutro com iluminação suave de estúdio"
        ]
    )

    iluminacao = st.selectbox(
        "Iluminação / Clima Visual:",
        [
            "Luz natural e suave de janela",
            "Iluminação de estúdio limpa e brilhante",
            "Luz quente e aconchegante de fim de tarde (Golden Hour)"
        ]
    )

    if "POV" in tipo_plano or "Transição" in tipo_plano or "Sapato" in tipo_plano:
        detalhes_membro = st.text_input(
            "Detalhes das Mãos:",
            value="mãos femininas com unhas compridas decoradas, anéis delicados e pulseira"
        )
    else:
        detalhes_membro = st.text_input(
            "Vestuário / Estilo do Modelo:",
            value="look casual moderno e neutro"
        )

    acao_dinamica = st.text_input(
        "Ação Complementar:",
        placeholder="Ex: sorrindo, virando de lado, ajeitando a roupa..."
    )

    st.markdown("---")
    st.info("🤐 **Vídeo 100% Sem Fala:** A modelo apenas demonstra o produto visualmente.\n\n"
            "🎬 **Compatibilidade:** Funciona perfeitamente em ferramentas de IA baseadas em imagem/vídeo de referência.")

# ==========================================
# COLUNA 3: OUTPUT DO PROMPT UNIFICADO
# ==========================================
with col_right:
    st.subheader("📋 Prompt Unificado (Vídeo Completo)")

    prompt_unificado = []

    # 1. Formato, Ritmo e Ausência de Fala
    if "Foto" in tipo_midia:
        prompt_unificado.append("Fotografia comercial de produto em alta resolução, proporção vertical 9:16.")
    else:
        prompt_unificado.append("Vídeo clipe vertical 9:16 ultra-realista e contínuo no estilo UGC do TikTok, totalmente silencioso (sem fala), focado na demonstração visual.")

    if "Câmera Lenta" in ritmo_duracao:
        prompt_unificado.append("Movimentos de câmera e ações em câmera lenta (slow motion 0.5x), estendendo a duração da cena e mantendo fluidez pausada.")
    elif "Suave" in ritmo_duracao:
        prompt_unificado.append("Movimento de câmera suave, cadenciado e de longa duração.")

    # 2. Lógica do Estilo Selecionado
    if "Dancinha Viral" in tipo_plano:
        prompt_unificado.append(
            f"A modelo da imagem de referência veste o(a) {produto_nome if produto_nome else 'roupa/conjunto'} "
            f"conforme mostrado na foto do produto. Ela realiza os movimentos exatos, ritmo e passos da dancinha viral "
            f"do vídeo de referência anexado, dançando alegremente em {cenario.lower()}. "
            f"A câmera permanece estável acompanhando a coreografia, com foco nítido na roupa em movimento e no caimento da peça no corpo da modelo."
        )

    elif "Transição POV" in tipo_plano:
        unboxing_str = f"rasgando a embalagem plástica transparente com calma, retirando o(a) {produto_nome if produto_nome else 'produto'} de dentro e " if embalagem_efeito else ""
        prompt_unificado.append(
            f"A CENA COMEÇA com visão em primeira pessoa (POV) vista de cima das {detalhes_membro.lower()} {unboxing_str}"
            f"organizando e estendendo o(a) {produto_nome if produto_nome else 'roupa'} cuidadosamente sobre {cenario.lower()}, exbindo os detalhes da peça. "
            f"EM SEGUIDA, HÁ UMA TRANSIÇÃO COM CORTE RÁPIDO (JUMP CUT) para a modelo da foto de referência vestindo "
            f"o(a) mesmo(a) {produto_nome if produto_nome else 'roupa'} em pé em frente ao espelho de corpo inteiro, gravando um vídeo de selfie. "
            f"Ela se vira suavemente mostrando o ajuste, caimento e detalhes da peça no corpo sem falar."
        )

    elif "Sapato" in tipo_plano:
        prompt_unificado.append(
            f"A CENA COMEÇA em perspectiva em primeira pessoa (POV) vista de cima das {detalhes_membro.lower()} "
            f"abrindo a caixa de calçado sobre {cenario.lower()}, retirando o(a) {produto_nome if produto_nome else 'sapato/tênis'} "
            f"de dentro da caixa e girando a peça lentamente nas mãos para mostrar em close-up o design, textura, costuras, solado e detalhes do modelo. "
            f"NA SEQUÊNCIA, HÁ UMA TRANSIÇÃO COM CORTE RÁPIDO para a modelo vestindo o(a) mesmo(a) {produto_nome if produto_nome else 'sapato/tênis'} "
            f"em pé em frente ao espelho de corpo inteiro. A câmera faz um zoom aproximado focado nos pés para mostrar o calçado no pé, "
            f"enquanto ela gira levemente o tornozelo exibindo a peça em uso sem falar."
        )

    elif "Múltiplas Cores" in tipo_plano:
        prompt_unificado.append(
            f"Vídeo de exibição de produto sem fala com CÂMERA FIXA em tripé focada na modelo em {cenario.lower()}, "
            f"olhando para a câmera e sorrindo enquanto passa a mão suavemente pelo corpo mostrando o caimento do(a) {produto_nome if produto_nome else 'roupa/conjunto'}. "
            f"O VÍDEO CONTÉM TRANSIÇÕES RÁPIDAS E FLUIDAS (JUMP CUTS) onde a modelo permanece na mesma posição e enquadramento, "
            f"mas alternando consecutivamente entre as diferentes variações de cores da mesma peça apresentadas nas imagens de referência anexadas, "
            f"destacando toda a cartela de cores disponíveis para o produto."
        )

    elif "Showcase Model" in tipo_plano:
        prompt_unificado.append(
            f"A CENA COMEÇA com um movimento dinâmico de câmera em 360 graus girando lentamente ao redor da personagem vestindo {detalhes_membro.lower()} sem fala. "
            f"A CÂMERA ENTÃO APROXIMA EM ZOOM LENTO para mostrar em close-up a textura do tecido, costuras, acabamento e detalhes de perto do(a) {produto_nome if produto_nome else 'produto'}."
        )

    elif "POV" in tipo_plano:
        unboxing_str = f"PRIMEIRO, as mãos rasgam a embalagem plástica transparente com calma, retiram o(a) {produto_nome if produto_nome else 'produto'} de dentro e o(a) posicionam cuidadosamente sobre {cenario.lower()}. " if embalagem_efeito else ""
        prompt_unificado.append(
            f"Perspectiva em primeira pessoa (POV) vista de cima em ritmo lento apresentando {detalhes_membro.lower()} interagindo com a peça sem fala. "
            f"{unboxing_str}A câmera faz um zoom suave de aproximação enquanto as mãos passam os dedos sobre o tecido, exibindo as costuras e texturas de perto em câmera lenta."
        )

    else:
        prompt_unificado.append(
            f"Apresentando a personagem da imagem de referência vestindo {detalhes_membro.lower()} e mostrando o(a) {produto_nome if produto_nome else 'produto'} sem fala. "
        )
        if embalagem_efeito:
            prompt_unificado.append(
                f"As mãos rasgam a embalagem plástica transparente com calma, retiram o produto e o posicionam sobre {cenario.lower()}. "
                f"Em seguida, a modelo exibe de perto os detalhes da peça."
            )
        elif acao_dinamica:
            prompt_unificado.append(f"Ação: {acao_dinamica}.")

    # 3. Finalização de Qualidade
    prompt_unificado.append(
        f"Cenário: {cenario.lower()}. {iluminacao}, foco nítido no produto, vídeo 100% silencioso (sem fala e sem textos em tela), ultra alta resolução, estética comercial limpa estilo UGC."
    )

    prompt_completo_texto = " ".join(prompt_unificado)

    # Exibição do Prompt
    st.markdown("**Prompt Unificado para a IA de Vídeo:**")
    st.code(prompt_completo_texto, language="markdown")

    # Orientação de Aplicação
    if "Dancinha" in tipo_plano:
        st.info(
            "💡 **Como usar para Dancinha Viral:**\n"
            "Anexe na sua ferramenta de IA:\n"
            "1. Foto da Modelo\n"
            "2. Foto da Roupa\n"
            "3. Vídeo de Referência da Dança do TikTok"
        )
    else:
        st.info(
            "💡 **Como Usar este Prompt:**\n"
            "Anexe a foto da modelo e a foto da roupa/produto na ferramenta de IA e cole o texto acima."
        )
