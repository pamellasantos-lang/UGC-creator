import streamlit as st

# 1. Configuração da página em Modo Wide
st.set_page_config(
    page_title="UGC Ad Studio - Modular Prompt",
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
st.caption("Crie prompts focados em ações e cenários para usar combinados com fotos do seu Personagem + Produto.")

st.markdown("---")

col_left, col_mid, col_right = st.columns([1, 1.1, 1], gap="medium")

# ==========================================
# COLUNA 1: ENQUADRAMENTO E MÍDIA BASE
# ==========================================
with col_left:
    st.subheader("🎯 Formato & Produto")

    tipo_plano = st.selectbox(
        "Perspectiva da Câmera:",
        [
            "Visão POV (Apenas Mãos em Primeira Pessoa)",
            "Modelo em Cena - Close-up (Rosto / Busto)",
            "Modelo em Cena - Corpo Inteiro (Lifestyle)",
            "Selfie no Espelho / Câmera Frontal"
        ],
        help="(i) Define se o vídeo focará apenas nas mãos (POV) ou na personagem inteira."
    )

    produto_nome = st.text_input(
        "Nome / Categoria do Produto:",
        placeholder="Ex: Pijama de coração, Sérum facial, Garrafa térmica...",
        help="(i) Identificação do produto para contextualizar no prompt."
    )

    embalagem_efeito = st.checkbox(
        "Efeito Unboxing (Saco plástico transparente)",
        value=False,
        help="(i) Ative para incluir a ação de abrir ou retirar o produto de uma embalagem plástica."
    )

    ferramenta_destino = st.selectbox(
        "Ferramenta de IA Destino:",
        [
            "Kling AI / Luma Dream Machine (Vídeo Direto)",
            "Midjourney / Flux (Para criar Imagem Base primeiro)",
            "Runway Gen-3 / Hailuo AI"
        ],
        help="(i) Ajusta a estrutura das instruções conforme a IA que você utilizará."
    )

# ==========================================
# COLUNA 2: AMBIENTE E AÇÕES
# ==========================================
with col_mid:
    st.subheader("⚡ Cenario & Ação")

    cenario = st.selectbox(
        "Ambiente / Cenário:",
        [
            "Cama com edredom neutro e tapete felpudo branco",
            "Quarto moderno e iluminado com luz de janela",
            "Penteadeira / Banheiro de luxo com espelho",
            "Mesa minimalista de mármore",
            "Ambiente interno neutro com fundo suavemente desfocado"
        ],
        help="(i) Local onde a cena acontece."
    )

    iluminacao = st.selectbox(
        "Iluminação / Clima Visual:",
        [
            "Luz natural e suave de janela (Soft Window Light)",
            "Iluminação de estúdio limpa e brilhante",
            "Luz quente e aconchegante de fim de tarde"
        ]
    )

    if "POV" in tipo_plano:
        detalhes_membro = st.text_input(
            "Detalhes das Mãos:",
            value="Mãos femininas com unhas longas decoradas e anéis delicados",
            help="(i) Características visuais das mãos que interagem com o produto."
        )
    else:
        detalhes_membro = st.text_input(
            "Estilo de Roupa da Personagem:",
            value="Roupa casual e neutra",
            help="(i) Vestuário para harmonizar com a cena."
        )

    acao_dinamica = st.text_input(
        "Ação Principal com o Produto:",
        placeholder="Ex: Segurando com cuidado, dobrando o tecido, virando o rótulo...",
        help="(i) Movimento exato que deve ocorrer na animação."
    )

    cta_choice = st.radio(
        "Botão de CTA (TikTok Preview):",
        ["Compre Aqui 🛒", "Saiba Mais 🔗", "Ganta o Seu 🎁"],
        horizontal=True
    )

# ==========================================
# COLUNA 3: PROMPT GERADO E TIKTOK PREVIEW
# ==========================================
with col_right:
    st.subheader("📋 Prompt Pronto para Copiar")

    # Estrutura modular sem prescrever a identidade exata da modelo no texto
    prompt_elements = []

    if "POV" in tipo_plano:
        prompt_elements.append("Aesthetic 9:16 vertical video clip, top-down POV first-person perspective.")
        prompt_elements.append(f"Featuring {detalhes_membro.lower()} interacting directly with the product shown in the attached reference image ({produto_nome if produto_nome else 'product'}).")
        
        if embalagem_efeito:
            prompt_elements.append("The hands are carefully taking the item out of a clear transparent plastic package.")
        else:
            prompt_elements.append(f"Action: {acao_dinamica if acao_dinamica else 'gracefully displaying and touching the product'}.")
            
        prompt_elements.append(f"Set on a {cenario.lower()}.")

    else:
        prompt_elements.append("Realistic 9:16 vertical video clip.")
        prompt_elements.append(f"Featuring the character from the attached reference image wearing {detalhes_membro.lower()}, holding and presenting the product from the second reference image ({produto_nome if produto_nome else 'product'}).")
        
        if embalagem_efeito:
            prompt_elements.append("Action: Opening a clear plastic polybag package to show the product inside.")
        else:
            prompt_elements.append(f"Action: {acao_dinamica if acao_dinamica else 'smiling gently and showing the product directly to the camera'}.")
            
        prompt_elements.append(f"Setting: {cenario.lower()}.")

    prompt_elements.append(f"{iluminacao}, sharp product focus, ultra high resolution, clean commercial UGC aesthetic.")

    prompt_final = " ".join(prompt_elements)

    st.markdown("**Instruções de Anexo na IA:**")
    st.info("📎 **Imagem 1:** Foto da Personagem / Mãos\n\n📎 **Imagem 2:** Foto do Produto")

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
                    <p style="font-size: 26px; margin-bottom: 5px;">🎬</p>
                    <p class="tiktok-text" style="font-weight: bold; color: #38BDF8 !important;">CENA DINÂMICA</p>
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
                    <p class="tiktok-text" style="font-size: 10px !important; color: #D1D5DB !important;">Plano: {tipo_plano.split('-')[0]}</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
