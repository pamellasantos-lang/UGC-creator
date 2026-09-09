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
st.caption("Crie prompts unificados em português com unboxing, transições, zoom de detalhes e CTA fixo apontando para baixo.")

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
            "Transição Viral - Unboxing na Cama ➔ Provador no Espelho (Try-On)",
            "Visão POV (Apenas Mãos em Primeira Pessoa)",
            "Showcase Model - Câmera 360° em Volta (Giro + Zooms de Detalhes da Peça)",
            "Modelo em Cena - Close-up (Rosto / Busto)",
            "Modelo em Cena - Corpo Inteiro (Lifestyle)",
            "Selfie no Espelho / Câmera Frontal"
        ],
        help="(i) 'Transição Viral' cria um vídeo duplo: unboxing seguido de um corte rápido da modelo vestindo o look no espelho."
    )

    if "Showcase" in tipo_plano:
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
        placeholder="Ex: Conjunto de Pijama de Coração, Camiseta Oversized...",
        help="(i) Identificação do produto para contextualizar no prompt."
    )

    embalagem_efeito = st.checkbox(
        "Efeito Unboxing (Rasgar embalagem plástica e posicionar na cama)",
        value=True,
        help="(i) Ative para incluir a ação das mãos rasgando a embalagem plástica, tirando a peça e arrumando-a na cama."
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

    if "POV" in tipo_plano or "Transição" in tipo_plano:
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
        placeholder="Ex: se virando suavemente no espelho, mostrando o tecido de perto..."
    )

    st.markdown("---")
    st.info("🛒 **CTA Fixo:** A chamada para ação está travada para a modelo/mãos apontarem para baixo no final do vídeo ('Compre Aqui 👇').")

# ==========================================
# COLUNA 3: OUTPUT DO PROMPT UNIFICADO
# ==========================================
with col_right:
    st.subheader("📋 Prompt Unificado (Vídeo Completo)")

    prompt_unificado = []

    # 1. Formato e Ritmo
    if "Foto" in tipo_midia:
        prompt_unificado.append("Fotografia comercial de produto em alta resolução, proporção vertical 9:16.")
    else:
        prompt_unificado.append("Vídeo clipe vertical 9:16 ultra-realista e contínuo no estilo UGC viral do TikTok.")

    if "Câmera Lenta" in ritmo_duracao:
        prompt_unificado.append("Movimentos de câmera e ações em câmera lenta (slow motion 0.5x), estendendo a duração da cena e mantendo fluidez pausada.")
    elif "Suave" in ritmo_duracao:
        prompt_unificado.append("Movimento de câmera suave, cadenciado e de longa duração.")

    # 2. Ação Inicial + Transição / Exibição
    if "Transição Viral" in tipo_plano:
        prompt_unificado.append(
            f"A CENA COMEÇA com perspectiva em primeira pessoa (POV) vista de cima das {detalhes_membro.lower()} "
            f"rasgando a embalagem plástica transparente com calma, retirando o(a) {produto_nome if produto_nome else 'produto'} "
            f"de dentro e arrumando a peça sobre {cenario.lower()}, exatamente como mostrado na foto de referência. "
            f"EM SEGUIDA, HÁ UMA TRANSIÇÃO COM CORTE RÁPIDO (JUMP CUT) onde a modelo da foto de referência aparece vestindo "
            f"o(a) mesmo(a) {produto_nome if produto_nome else 'produto'}, gravando um vídeo de selfie no espelho de corpo inteiro com seu smartphone. "
            f"Ela se vira suavemente mostrando o caimento do produto e o ajuste no corpo."
        )

    elif "Showcase" in tipo_plano:
        prompt_unificado.append(
            f"A CENA COMEÇA com um movimento dinâmico de câmera em 360 graus girando lentamente ao redor da personagem vestindo {detalhes_membro.lower()}. "
            f"A CÂMERA ENTÃO APROXIMA EM ZOOM LENTO para mostrar em close-up a textura do tecido, costuras, acabamento e detalhes de perto do(a) {produto_nome if produto_nome else 'produto'}."
        )

    elif "POV" in tipo_plano:
        prompt_unificado.append(
            f"Perspectiva em primeira pessoa (POV) vista de cima em ritmo lento apresentando {detalhes_membro.lower()} interagindo com a peça. "
        )
        if embalagem_efeito:
            prompt_unificado.append(
                f"PRIMEIRO, as mãos rasgam a embalagem plástica transparente com calma, retiram o(a) {produto_nome if produto_nome else 'produto'} "
                f"de dentro e o(a) posicionam cuidadosamente sobre {cenario.lower()}, estendendo a peça sobre a superfície. "
                f"NA SEQUÊNCIA DA MESMA CENA, a câmera faz um zoom suave de aproximação enquanto as mãos passam os dedos sobre o tecido, "
                f"exibindo as costuras, estampa e texturas de perto em câmera lenta."
            )
        else:
            prompt_unificado.append(
                f"As mãos exibem e tocam o(a) {produto_nome if produto_nome else 'produto'} suavemente, "
                f"virando a peça devagar para mostrar as costuras, tecido e acabamentos em um zoom aproximado de alta definição."
            )

    else:
        prompt_unificado.append(
            f"Apresentando a personagem da imagem de referência vestindo {detalhes_membro.lower()} e mostrando o(a) {produto_nome if produto_nome else 'produto'}. "
        )
        if embalagem_efeito:
            prompt_unificado.append(
                f"As mãos rasgam a embalagem plástica transparente com calma, retiram o produto e o posicionam sobre {cenario.lower()}. "
                f"Em seguida, a modelo exibe de perto os detalhes da peça."
            )
        elif acao_dinamica:
            prompt_unificado.append(f"Ação: {acao_dinamica}.")

    # 3. CTA Visual Fixo no Final (Sem opção de alteração)
    prompt_unificado.append(
        "NOS ÚLTIMOS 2 SEGUNDOS DO VÍDEO, a cena faz uma pausa sutil e traz um gesto/indicação visual direta "
        "apontando claramente para a parte inferior central da tela (direcionando o olhar para baixo em direção ao botão de compra do TikTok Shop) "
        "com indicação de seta e legenda dizendo 'Compre Aqui 👇'."
    )

    # 4. Finalização de Qualidade e Ambiente
    prompt_unificado.append(
        f"Cenário: {cenario.lower()}. {iluminacao}, foco nítido no produto, ultra alta resolução, estética comercial limpa estilo UGC."
    )

    prompt_completo_texto = " ".join(prompt_unificado)

    # Exibição do Prompt
    st.markdown("**Prompt Único (Sequência Completa + Unboxing + Detalhes + CTA Fixo Apontando para Baixo):**")
    st.code(prompt_completo_texto, language="markdown")

    # Orientação de Aplicação
    st.info(
        "💡 **Como Usar este Prompt Unificado:**\n\n"
        "1. Na sua ferramenta de IA (Kling AI, Luma, Google Flow, Meta AI), anexe a foto do produto e/ou modelo.\n"
        "2. Cole todo o texto gerado acima em um único campo de prompt.\n"
        "3. A chamada para ação está pré-configurada para que a ação finalize apontando para baixo ('Compre Aqui 👇')."
    )
