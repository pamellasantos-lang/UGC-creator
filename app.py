import streamlit as st

# 1. Configuração da página em Modo Wide
st.set_page_config(
    page_title="UGC Ad Studio - Gerador Modular",
    page_icon="🎬",
    layout="wide"
)

# 2. Estilização CSS de Alta Visibilidade (Estúdio Claro Pro)
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
    .phone-wrapper {
        display: flex;
        justify-content: center;
        margin-top: 15px;
    }
    .tiktok-card {
        width: 260px;
        height: 450px;
        background: linear-gradient(180deg, #1E293B 0%, #0F172A 100%);
        border: 4px solid #334155;
        border-radius: 24px;
        position: relative;
        overflow: hidden;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
    }
    .tiktok-badge {
        position: absolute;
        top: 12px;
        left: 12px;
        background: rgba(15, 23, 42, 0.8);
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 10px;
        font-weight: bold;
        color: #38BDF8 !important;
        border: 1px solid #38BDF8;
    }
    .tiktok-sidebar {
        position: absolute;
        right: 10px;
        bottom: 70px;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 12px;
    }
    .tiktok-icon-btn {
        background: rgba(255, 255, 255, 0.15);
        width: 32px;
        height: 32px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 13px;
    }
    .tiktok-bottom {
        position: absolute;
        bottom: 12px;
        left: 12px;
        right: 55px;
    }
    .shop-tag {
        background: #FE2C55;
        color: #FFFFFF !important;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 10px;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 6px;
    }
    .tiktok-text {
        font-size: 11px !important;
        line-height: 1.2 !important;
        margin: 0 !important;
        color: #F8FAFC !important;
    }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho
st.title("🎬 UGC Ad Studio - Gerador Modular")
st.caption("Crie prompts otimizados para Fotos Base ou Vídeos Dinâmicos combinando Personagem + Produto.")

st.markdown("---")

col_left, col_mid, col_right = st.columns([1, 1.1, 1], gap="medium")

# ==========================================
# COLUNA 1: FORMATO, TIPO DE MÍDIA E FERRAMENTA
# ==========================================
with col_left:
    st.subheader("🎯 Mídia & Formato")

    tipo_midia = st.selectbox(
        "Formato do Prompt Desejado:",
        [
            "Gerar Foto / Imagem Base (Para animar posteriormente)",
            "Gerar Vídeo Direto (Com movimento e ação)"
        ],
        help="(i) Escolha 'Foto' caso queira primeiro criar a imagem estática perfeita do produto/modelo para usar como referência no vídeo."
    )

    tipo_plano = st.selectbox(
        "Perspectiva / Estilo da Câmera:",
        [
            "Showcase Model - Câmera 360° em Volta (Giro + Zooms de Detalhes da Peça)",
            "Visão POV (Apenas Mãos em Primeira Pessoa)",
            "Modelo em Cena - Close-up (Rosto / Busto)",
            "Modelo em Cena - Corpo Inteiro (Lifestyle)",
            "Selfie no Espelho / Câmera Frontal"
        ],
        help="(i) Escolha 'Showcase Model' para simular alguém filmando ao redor do modelo com aproximações e zooms nos detalhes da peça."
    )

    # Condicional para detalhes de peças no modo Showcase
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
        placeholder="Ex: Camiseta amarela Oversized, Tênis esportivo, Sérum...",
        help="(i) Identificação do produto para contextualizar no prompt."
    )

    embalagem_efeito = st.checkbox(
        "Efeito Unboxing (Saco plástico transparente)",
        value=False,
        help="(i) Ative se quiser incluir a ação de abrir ou tirar o produto da embalagem."
    )

    ferramenta_destino = st.selectbox(
        "Ferramenta de IA Destino (Foco Gratuito):",
        [
            "Meta AI / WhatsApp AI (100% Gratuito)",
            "Google Flow / Veo (Gratuito / Acesso Grátis)",
            "Kling AI (Créditos Diários Grátis)",
            "Luma Dream Machine (Créditos Grátis)",
            "Runway Gen-3 / Hailuo AI (Testes Grátis)",
            "Flux / Midjourney (Criação de Imagem Base)"
        ],
        help="(i) Selecione a ferramenta para adaptar o formato do comando."
    )

# ==========================================
# COLUNA 2: CENÁRIO E AÇÕES
# ==========================================
with col_mid:
    st.subheader("⚡ Cenário & Detalhes")

    cenario = st.selectbox(
        "Ambiente / Cenário:",
        [
            "Cama com edredom neutro e tapete felpudo branco",
            "Quarto moderno e iluminado com luz natural de janela",
            "Penteadeira / Banheiro de luxo com espelho",
            "Mesa minimalista de mármore",
            "Cenário urbano / Rua moderna com estática clean",
            "Fundo neutro com iluminação suave de estúdio"
        ],
        help="(i) Local onde a cena ou foto acontecerá."
    )

    iluminacao = st.selectbox(
        "Iluminação / Clima Visual:",
        [
            "Luz natural e suave de janela (Soft Window Light)",
            "Iluminação de estúdio limpa e brilhante",
            "Luz quente e aconchegante de fim de tarde (Golden Hour)"
        ]
    )

    if "POV" in tipo_plano:
        detalhes_membro = st.text_input(
            "Detalhes das Mãos:",
            value="Mãos femininas com unhas longas decoradas e anéis delicados",
            help="(i) Estilo das mãos ao interagir com a peça."
        )
    else:
        detalhes_membro = st.text_input(
            "Vestuário / Estilo do Modelo:",
            value="Look casual moderno e neutro",
            help="(i) Roupas e estilo do modelo na cena."
        )

    acao_dinamica = st.text_input(
        "Ação / Movimento Adicional:",
        placeholder="Ex: Virando levemente de lado, ajeitando a gola, caminhando devagar...",
        help="(i) Movimento sutil do modelo ou da ação na cena."
    )

    cta_choice = st.radio(
        "Botão de CTA (TikTok Preview):",
        ["Compre Aqui 🛒", "Saiba Mais 🔗", "Garanta o Seu 🎁"],
        horizontal=True
    )

# ==========================================
# COLUNA 3: OUTPUT E SIMULADOR
# ==========================================
with col_right:
    st.subheader("📋 Prompt Pronto para Copiar")

    prompt_elements = []

    # 1. Definição se é Foto ou Vídeo
    if "Foto" in tipo_midia:
        prompt_elements.append("High-resolution commercial product photograph, vertical 9:16 aspect ratio.")
    else:
        prompt_elements.append("Realistic 9:16 vertical video clip, smooth cinematic motion.")

    # 2. Definição do Tipo de Câmera / Perspectiva
    if "Showcase" in tipo_plano:
        prompt_elements.append("Dynamic 360-degree camera movement smoothly panning around the model.")
        
        if tipo_peca:
            if "Blusa" in tipo_peca:
                prompt_elements.append(f"Includes close-up zoom shots emphasizing the fabric texture, collar design, stitching, and fit of the {produto_nome if produto_nome else 'shirt/top'}.")
            elif "Bermuda" in tipo_peca:
                prompt_elements.append(f"Includes detailed zoom-in shots highlighting the pockets, waistband, waist fit, and material texture of the {produto_nome if produto_nome else 'pants/shorts'}.")
            elif "Tênis" in tipo_peca:
                prompt_elements.append(f"Includes sharp close-up zoom shots focusing on the shoe sole, side details, laces, and footwear material of the {produto_nome if produto_nome else 'sneakers/shoes'}.")
            else:
                prompt_elements.append(f"Includes detailed close-up zooms highlighting key features of the {produto_nome if produto_nome else 'outfit'}.")

        prompt_elements.append(f"Featuring the character from the attached reference image wearing {detalhes_membro.lower()}.")

    elif "POV" in tipo_plano:
        prompt_elements.append("Top-down POV first-person perspective.")
        prompt_elements.append(f"Featuring {detalhes_membro.lower()} interacting directly with the product shown in the reference image ({produto_nome if produto_nome else 'product'}).")
        
        if embalagem_efeito:
            prompt_elements.append("The hands are carefully taking the item out of a clear transparent plastic package.")
        else:
            prompt_elements.append(f"Action: {acao_dinamica if acao_dinamica else 'displaying and touching the product'}.")

    else:
        prompt_elements.append(f"Featuring the character from the reference image wearing {detalhes_membro.lower()}, holding or wearing the {produto_nome if produto_nome else 'product'}.")
        if acao_dinamica:
            prompt_elements.append(f"Action: {acao_dinamica}.")

    # 3. Finalização do Prompt
    prompt_elements.append(f"Setting: {cenario.lower()}. {iluminacao}, sharp product focus, ultra high resolution, clean commercial UGC aesthetic.")

    prompt_final = " ".join(prompt_elements)

    # Instruções de Uso
    st.markdown("**Como Aplicar o Prompt:**")
    if "Foto" in tipo_midia:
        st.info("🖼️ **Modo Foto Selecionado:** Anexe a imagem da modelo + produto e cole o prompt na IA para gerar a imagem base perfeita.")
    else:
        st.info("🎥 **Modo Vídeo Selecionado:** Anexe as imagens de referência e cole o prompt direto na IA de animação (Meta AI, Kling, Luma, Google Flow).")

    st.markdown("**Prompt Gerado:**")
    st.code(prompt_final, language="markdown")

    st.markdown("---")
    st.markdown("**Simulador de Tela (TikTok 9:16)**")

    st.markdown(
        f"""
        <div class="phone-wrapper">
            <div class="tiktok-card">
                <div class="tiktok-badge">PREVIEW 9:16</div>
                <div style="position: absolute; top: 38%; left: 10%; right: 10%; text-align: center;">
                    <p style="font-size: 26px; margin-bottom: 5px;">{"🖼️" if "Foto" in tipo_midia else "🎬"}</p>
                    <p class="tiktok-text" style="font-weight: bold; color: #38BDF8 !important;">{"FOTO ESTÁTICA" if "Foto" in tipo_midia else "VÍDEO SHOWCASE"}</p>
                    <p class="tiktok-text" style="font-size: 10px !important; color: #9CA3AF !important;">{produto_nome if produto_nome else 'Produto'}</p>
                </div>
                <div class="tiktok-sidebar">
                    <div class="tiktok-icon-btn">❤️</div>
                    <div class="tiktok-icon-btn">💬</div>
                    <div class="tiktok-icon-btn">🔖</div>
                </div>
                <div class="tiktok-bottom">
                    <div class="shop-tag">{cta_choice}</div>
                    <p class="tiktok-text" style="font-weight: bold;">@ugc.studio</p>
                    <p class="tiktok-text" style="font-size: 10px !important; color: #D1D5DB !important;">Foco: {tipo_plano.split('-')[0]}</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
