import os
import streamlit as st

# 1. Configuração da página em Modo Wide
st.set_page_config(
    page_title="UGC Ad Studio - Multi-Creator",
    page_icon="🎬",
    layout="wide"
)

# 2. Estilização CSS de Alto Contraste (Dark Theme Pro)
st.markdown("""
    <style>
    /* Fundo Escuro Pro */
    .stApp {
        background-color: #0D1117;
        color: #F0F6FC;
    }

    /* Rótulos de Texto e Títulos */
    label, p, h1, h2, h3, h4, span, div {
        color: #F0F6FC !important;
        font-weight: 500;
    }

    /* Caixas de Entrada (Inputs/Selects) com fundo escuro e texto limpo */
    .stTextInput input, .stSelectbox div[data-baseweb="select"], .stTextArea textarea {
        background-color: #161B22 !important;
        color: #FFFFFF !important;
        border: 1px solid #30363D !important;
        border-radius: 6px !important;
    }

    /* Texto do Placeholder (Exemplo de fundo dentro do campo) */
    .stTextInput input::placeholder, .stTextArea textarea::placeholder {
        color: #8B949E !important;
        opacity: 1 !important;
    }

    /* Bloco do Prompt Formatado (Caixa de Cópia em Alto Contraste) */
    div[data-testid="stCodeBlock"] pre {
        background-color: #161B22 !important;
        border: 1px solid #30363D !important;
        border-radius: 8px !important;
    }
    div[data-testid="stCodeBlock"] code {
        color: #38BDF8 !important; /* Azul Neon claro de altíssima leitura */
        font-family: 'Fira Code', 'Courier New', monospace !important;
        font-size: 13px !important;
        line-height: 1.5 !important;
    }

    /* SIMULADOR TIKTOK 9:16 */
    .phone-wrapper {
        display: flex;
        justify-content: center;
        margin-top: 15px;
    }
    .tiktok-card {
        width: 260px;
        height: 460px;
        background: linear-gradient(180deg, #1F2937 0%, #111827 100%);
        border: 4px solid #374151;
        border-radius: 20px;
        position: relative;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(0,0,0,0.7);
    }
    .tiktok-badge {
        position: absolute;
        top: 12px;
        left: 12px;
        background: rgba(0, 0, 0, 0.6);
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
        background: rgba(0, 0, 0, 0.4);
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
        padding: 3px 8px;
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
        color: #E6EDF3 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- CABEÇALHO DO STUDIO ---
st.title("🎬 UGC Ad Studio")
st.caption("Estúdio de criação de prompts e roteiros para vídeos de produtos com múltiplos criadores.")

st.markdown("---")

# --- LAYOUT EM 3 COLUNAS PARALELAS ---
col_left, col_mid, col_right = st.columns([1, 1.1, 1], gap="medium")

# ==========================================
# COLUNA 1: INPUTS BÁSICOS & MODELO
# ==========================================
with col_left:
    st.subheader("👤 Modelo & Produto")

    # Seleção Flexível de Criadores
    perfil_modelo = st.selectbox(
        "Selecione o Criador / Influencer:",
        [
            "Aline - Latina / Brunette Lifestyle",
            "Visão POV - Mãos & Unboxing (Sem Rosto)",
            "Sarah - Blonde / Fitness & Wellness",
            "Maya - Asian / Clean Beauty Minimalist",
            "Modelo Personalizado (Inserir descrição própria)"
        ],
        help="(i) Escolha a modelo de referência para a campanha ou opte por 'Visão POV' para focar apenas em mãos e detalhes do produto."
    )

    # Descrição do Perfil do Influencer selecionado
    if "Aline" in perfil_modelo:
        desc_modelo = "Aline, a young Latina woman (approx. 24) with long dark brown hair, warm tan skin, glossy nude lips, gold chain necklace"
        ref_img_suggested = "aline rosto.jpeg / aline corpo.jpeg"
    elif "POV" in perfil_modelo:
        desc_modelo = "First-person POV top-down perspective showing only a woman's hands with decorated long nails and delicate jewelry"
        ref_img_suggested = "Nenhuma (Foco apenas em mãos e superfície)"
    elif "Sarah" in perfil_modelo:
        desc_modelo = "Sarah, a athletic 25-year-old blonde woman with natural makeup and glowing skin"
        ref_img_suggested = "sarah.jpeg"
    elif "Maya" in perfil_modelo:
        desc_modelo = "Maya, a stylish 22-year-old East Asian woman with sleek dark hair and elegant minimal aesthetic"
        ref_img_suggested = "maya.jpeg"
    else:
        desc_modelo = st.text_input(
            "Descreva o Modelo Personalizado:",
            placeholder="Ex: Homem de 30 anos, estilo casual...",
            help="(i) Digite as características físicas do modelo que a IA deve gerar."
        )
        ref_img_suggested = "foto_modelo_custom.jpeg"

    # Upload da Foto do Produto
    st.write("**Foto do Produto**")
    uploaded_product = st.file_uploader(
        "Arraste a foto do produto aqui",
        type=["png", "jpg", "jpeg"],
        help="(i) Faça o upload da imagem do produto que você deseja divulgar."
    )
    if uploaded_product:
        st.image(uploaded_product, caption="Produto Carregado", use_column_width=True)

    # Estilo de Enquadramento
    enquadramento = st.radio(
        "Foco de Enquadramento:",
        ["Close-up (Rosto / Mão)", "Corpo Inteiro (Lifestyle)", "POV / Plano Aberto (Mãos & Superfície)"],
        help="(i) Define o ângulo da câmera: focado no rosto, no corpo inteiro ou na visão das mãos em primeira pessoa."
    )

    # Tom da Campanha
    tom_campanha = st.selectbox(
        "Tom da Campanha:",
        ["Viral / Orgânico do TikTok", "Review Autêntico e Espontâneo", "Estética Luxuosa / Minimalista"],
        help="(i) Ajusta a iluminação e o ritmo visual do vídeo."
    )


# ==========================================
# COLUNA 2: WORKFLOW DE CONTEÚDO
# ==========================================
with col_mid:
    st.subheader("⚡ Workflow de Conteúdo")

    # Nome do Produto
    produto_nome = st.text_input(
        "Nome / Descrição do Produto:",
        placeholder="Ex: Camiseta amarela, Pijama de coração, Sérum facial...",
        help="(i) Escreva o nome exato do produto que aparecerá nas mãos do criador."
    )

    # 1. Gancho (Hook)
    st.markdown("#### 1. Gancho (Hook)")
    hook_type = st.selectbox(
        "Tipo de Gancho Inicial:",
        [
            "Segurando e apresentando o produto surpresa para a câmera",
            "Tirando o produto de um saco plástico transparente (Efeito Unboxing)",
            "Aplicando / Testando o produto diretamente em cena",
            "Mostrando a textura e detalhes do produto bem de perto"
        ],
        help="(i) Escolha a primeira ação nos 3 primeiros segundos do vídeo para prender a atenção do público."
    )

    # 2. Prova / Demonstração (Proof)
    st.markdown("#### 2. Prova / Demonstração (Proof)")
    cenario = st.selectbox(
        "Cenário / Ambientação:",
        [
            "Cama com edredom neutro e tapete felpudo branco",
            "Quarto moderno bem iluminado com luz natural de janela",
            "Penteadeira / Banheiro luxuoso com espelho iluminado",
            "Mesa minimalista de mármore com estética limpa"
        ],
        help="(i) Selecione onde o vídeo será gravado."
    )

    if "POV" in perfil_modelo:
        detalhes_estilo = st.text_input(
            "Estilo das Mãos / Acessórios:",
            value="Mãos com unhas compridas decoradas, anéis delicados e pulseira",
            help="(i) Detalhes visuais das mãos para garantir o visual estético no vídeo."
        )
    else:
        detalhes_estilo = st.text_input(
            "Vestuário do Criador (Outfit):",
            value="Vestido preto justo de alça fina",
            help="(i) Roupa ou estilo que o criador usará no vídeo."
        )

    acao_principal = st.text_input(
        "Ação Principal na Demonstração:",
        placeholder="Ex: Virando o produto, dobrando o tecido, passando a mão levemente...",
        help="(i) Descreva o movimento do criador ao demonstrar o produto durante o vídeo."
    )

    # 3. Chamada para Ação (CTA)
    st.markdown("#### 3. Chamada para Ação (CTA)")
    cta_choice = st.radio(
        "Botão de Chamada Final:",
        ["Shop Now 🛒", "Learn More 🔗", "Try It Today ✨", "Get Yours 🎁"],
        horizontal=True,
        help="(i) Selecione o texto e o estilo do botão de conversão no final do vídeo."
    )


# ==========================================
# COLUNA 3: OUTPUT E PREVIEW 9:16
# ==========================================
with col_right:
    st.subheader("📱 Preview & Output")

    # Montagem Dinâmica do Prompt Otimizado
    prompt_parts = [
        "UGC style vertical 9:16 video clip.",
        f"Featuring {desc_modelo}."
    ]

    if "POV" in perfil_modelo:
        prompt_parts.append(f"Set on a {cenario.lower()}.")
        prompt_parts.append(f"Action: {hook_type.lower()} with the {produto_nome if produto_nome else 'product'}.")
    else:
        prompt_parts.append(f"Wearing {detalhes_estilo}. Located in a {cenario.lower()}.")
        prompt_parts.append(f"Action: {hook_type.lower()} holding {produto_nome if produto_nome else 'the product'}.")

    if acao_principal:
        prompt_parts.append(f"Demonstration movement: {acao_principal}.")

    prompt_parts.append(f"Framing: {enquadramento.lower()}, {tom_campanha.lower()}, soft natural window light, sharp product focus, ultra high resolution.")

    prompt_final = " ".join(prompt_parts)

    st.markdown("**1. Imagem de Referência para a IA:**")
    st.code(ref_img_suggested, language="text")

    st.markdown("**2. Prompt Otimizado (Pronto para Copiar):**")
    st.code(prompt_final, language="markdown")

    st.markdown("---")
    st.markdown("**3. Simulador de Tela (TikTok / Reels 9:16)**")

    # Informações para o Simulador Visual
    prod_label = produto_nome if produto_nome else "Produto em Destaque"
    criador_label = perfil_modelo.split("-")[0].strip()

    st.markdown(
        f"""
        <div class="phone-wrapper">
            <div class="tiktok-card">
                <div class="tiktok-badge">PREVIEW 9:16</div>
                
                <div style="position: absolute; top: 38%; left: 10%; right: 10%; text-align: center;">
                    <p style="font-size: 26px; margin-bottom: 5px;">🎬</p>
                    <p class="tiktok-text" style="font-weight: bold; color: #38BDF8 !important;">{criador_label.upper()}</p>
                    <p class="tiktok-text" style="font-size: 10px !important; color: #9CA3AF !important;">Foco: {prod_label}</p>
                </div>

                <!-- Botões Laterais Interativos do TikTok -->
                <div class="tiktok-sidebar">
                    <div class="tiktok-icon-btn">❤️</div>
                    <div class="tiktok-icon-btn">💬</div>
                    <div class="tiktok-icon-btn">🔖</div>
                    <div class="tiktok-icon-btn">↪️</div>
                </div>

                <!-- Tag e Legenda do Produto -->
                <div class="tiktok-bottom">
                    <div class="shop-tag">🛒 {cta_choice}</div>
                    <p class="tiktok-text" style="font-weight: bold;">@{criador_label.lower().replace(' ', '')}.studio</p>
                    <p class="tiktok-text" style="font-size: 10px !important; color: #D1D5DB !important;">Gancho: {hook_type[:35]}...</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
