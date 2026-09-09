import streamlit as st

# 1. Configuração da página em modo Wide e título Studio
st.set_page_config(
    page_title="UGC Ad Studio - Aline",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Estilização CSS Dark Theme (Estilo Studio Pro)
st.markdown("""
    <style>
    /* Fundo Escuro do App */
    .stApp {
        background-color: #0d0f12;
        color: #e2e8f0;
    }
    
    /* Container Principal */
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    /* Cards e Caixas escuras */
    div[data-testid="stVerticalBlock"] > div {
        background-color: #161a22;
        border-radius: 12px;
        padding: 8px;
        border: 1px solid #232936;
    }

    /* Botões estilo Neon/Dark */
    .stButton>button {
        background-color: #232936;
        color: #e2e8f0;
        border: 1px solid #374151;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #4f46e5;
        color: white;
        border-color: #6366f1;
    }

    /* Inputs e Selectbox */
    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        background-color: #0d0f12 !important;
        color: #f3f4f6 !important;
        border: 1px solid #374151 !important;
        border-radius: 8px !important;
    }

    /* Header e Textos */
    h1, h2, h3, h4 {
        color: #ffffff !important;
        font-family: 'Inter', sans-serif;
    }

    /* Card de Preview do Vídeo */
    .video-preview-box {
        border: 2px solid #312e81;
        border-radius: 16px;
        background-color: #111827;
        padding: 15px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# --- IDENTIDADE FIXA DA ALINE ---
ALINE_CORE = (
    "realistic photograph of 'Aline,' a young Latina woman (approx. 24) with long dark brown hair, "
    "warm tan skin, detailed dark eyes, glossy nude lips, wearing a minimal gold chain necklace."
)

# --- HEADER DO STUDIO ---
st.title("🎬 UGC Ad Studio")
st.caption("Monte scripts, ângulos de gancho, prova social e gere prompts padronizados para a modelo Aline.")

st.markdown("---")

# --- LAYOUT EM 3 COLUNAS (Assim como no painel da imagem) ---
col_left, col_mid, col_right = st.columns([1, 1.3, 1])

# ==========================================
# PAINEL 1: CONFIGURAÇÕES E MODELO (ESQUERDA)
# ==========================================
with col_left:
    st.subheader("👤 Modelo & Produto")
    
    # Seleção de Modelo
    model_opt = st.selectbox("Modelo Ativo", ["Aline 2.0 (Latina / Studio)", "Aline (Carro / Lifestyle)"])
    
    # Upload do Produto
    st.write("**Upload do Produto**")
    uploaded_file = st.file_uploader("Arraste a foto do produto aqui", type=["png", "jpg", "jpeg"])
    
    if uploaded_file:
        st.image(uploaded_file, caption="Produto Carregado", use_column_width=True)
    else:
        st.info("📌 Envie uma foto do produto com fundo limpo.")

    # Avatar / Visual Focus
    st.write("**Foco de Enquadramento**")
    enquadramento = st.radio(
        "Estilo da Cena",
        ["Close-up (Rosto / Mão)", "Corpo Inteiro (Lifestyle)", "Espelho / Selfie"],
        horizontal=True
    )
    
    # Voice / Tone Settings
    st.selectbox("Tom da Campanha", ["Viral / Dinâmico", "Reviews Espontâneos", "Luxo / Estética Minimalista"])

# ==========================================
# PAINEL 2: CONTENT FLOW (CENTRO)
# ==========================================
with col_mid:
    st.subheader("⚡ Fluxo de Conteúdo (Content Flow)")
    
    # Hook Section
    st.markdown("#### 1. Gancho (Hook)")
    hook_type = st.selectbox(
        "Tipo de Gancho Inicial",
        [
            "Mostrando o produto de surpresa",
            "Segurando o produto próximo ao rosto com sorriso",
            "Aplicando/Experimentando o produto diretamente na câmera"
        ]
    )

    # Proof / Social Proof
    st.markdown("#### 2. Prova / Demonstração (Proof)")
    cenario_opcao = st.selectbox(
        "Cenário / Ambientação",
        [
            "Quarto moderno bem iluminado com luz suave",
            "Banheiro luxuoso / Penteadeira com espelho iluminado",
            "Ambiente interno neutro e minimalista"
        ]
    )
    
    outfit = st.text_input("Vestuário da Aline", value="vestido preto justo de alça fina")

    # Call to Action (CTA)
    st.markdown("#### 3. Chamada para Ação (CTA)")
    cta_choice = st.radio(
        "Texto do Botão / CTA Final",
        ["Shop Now", "Learn More", "Try It Today", "Get Yours"],
        horizontal=True
    )

# ==========================================
# PAINEL 3: PREVIEW E GERADOR (DIREITA)
# ==========================================
with col_right:
    st.subheader("📱 Preview & Prompt Final")
    
    # Montagem Dinâmica do Prompt
    st.markdown("**Prompt Gerado para IAs de Vídeo/Imagem:**")
    
    prompt_gerado = (
        f"UGC style ad, 9:16 vertical video frame. {ALINE_CORE} "
        f"Located in a {cenario_opcao.lower()}. She is wearing a {outfit}. "
        f"Action: {hook_type.lower()}, featuring the product prominently in focus. "
        f"Style: {enquadramento.lower()}, natural lighting, sharp details, realistic skin texture, high resolution."
    )
    
    # Exibição do Prompt
    st.code(prompt_gerado, language="markdown")
    
    # Simulador do Leitor/Player do TikTok (Preview Visual)
    st.markdown("---")
    st.markdown("**Simulação de Player (TikTok / Reels 9:16)**")
    
    with st.container():
        st.markdown(
            f"""
            <div class="video-preview-box">
                <p style="color: #a5b4fc; font-size: 12px; margin-bottom: 5px;">PREVIEW DA CENA</p>
                <div style="height: 180px; background-color: #1f2937; border-radius: 8px; display: flex; align-items: center; justify-content: center; flex-direction: column;">
                    <span style="font-size: 30px;">🎬</span>
                    <p style="font-size: 11px; color: #9ca3af; margin-top: 5px;">
                        Modelo: <b>Aline</b><br>
                        Ação: <b>{hook_type}</b><br>
                        CTA: <b>{cta_choice}</b>
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
