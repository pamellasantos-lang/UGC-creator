import os
import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="UGC Studio - Aline",
    page_icon="🎬",
    layout="wide"
)

# Estilização CSS de Alto Contraste + Simulador TikTok 9:16
st.markdown("""
    <style>
    /* Fundo Escuro Pro */
    .stApp {
        background-color: #0D1117;
        color: #F0F6FC;
    }

    /* Garantia de leitura para rótulos e textos */
    label, p, h1, h2, h3, h4, span, div {
        color: #F0F6FC !important;
        font-weight: 500;
    }

    /* Entradas de Texto e Modais */
    .stTextInput input, .stSelectbox div[data-baseweb="select"] {
        background-color: #161B22 !important;
        color: #FFFFFF !important;
        border: 1px solid #30363D !important;
        border-radius: 6px !important;
    }

    /* Texto de Exemplo (Placeholder) visível */
    .stTextInput input::placeholder {
        color: #8B949E !important;
        opacity: 1 !important;
    }

    /* Bloco do Prompt (Caixa de Cópia em Alto Contraste) */
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
        margin-top: 10px;
    }
    .tiktok-card {
        width: 270px;
        height: 480px;
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
        width: 34px;
        height: 34px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 14px;
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

st.title("🎬 UGC Studio - Aline")
st.caption("Gerador de Prompts e Prévia Visual Otimizados para TikTok & Reels.")

st.markdown("---")

col_left, col_right = st.columns([1.1, 1], gap="large")

# ==========================================
# COLUNA ESQUERDA: CAMPOS DE ENTRADA
# ==========================================
with col_left:
    st.subheader("⚙️ Configurações da Cena")

    estilo_cena = st.selectbox(
        "🎥 Estilo do Vídeo:",
        [
            "Visão POV - Mãos & Unboxing (Apenas mãos com joias e unhas decoradas)",
            "Close-up de Rosto (Aline segurando produto ao lado do rosto)",
            "Corpo Inteiro Lifestyle (Aline mostrando o produto no quarto)",
            "Selfie no Espelho (Aline mostrando produto / look inteiro)"
        ],
        help="(i) Escolha a perspectiva da câmera. 'POV' mostra apenas as mãos segurando o produto em cima de uma superfície. As demais opções mostram a modelo Aline."
    )

    produto_nome = st.text_input(
        "📦 Nome / Descrição do Produto:",
        placeholder="Ex: Camiseta amarela, Pijama de coração, Sérum facial...",
        help="(i) Digite exatamente o nome ou tipo do produto que será destacado no vídeo."
    )

    if "Visão POV" in estilo_cena:
        ref_image_name = "Nenhuma (Visão POV - Sem Rosto)"
        
        com_embalagem = st.checkbox(
            "📦 Efeito Unboxing (Retirando da embalagem plástica)",
            value=True,
            help="(i) Marque esta opção se quiser que a cena comece com as mãos abrindo um saco plástico transparente e tirando o produto de dentro."
        )

        cenario_pov = st.selectbox(
            "🛏️ Cenário de Fundo (POV):",
            [
                "Cama com edredom neutro e tapete felpudo branco",
                "Chão de madeira clara com tapete felpudo branco",
                "Mesa minimalista de mármore com iluminação natural"
            ],
            help="(i) Define qual será o plano de fundo onde o produto e as mãos vão aparecer."
        )

        detalhes_maos = st.text_input(
            "💅 Detalhes das Mãos & Acessórios:",
            value="Mãos com unhas compridas bem pintadas e decoradas, usando anéis delicados, pulseira e relógio",
            help="(i) Especifique o estilo das unhas e joias para manter a estética das mãos no vídeo."
        )
        outfit = ""
    else:
        com_embalagem = False
        cenario_pov = ""
        detalhes_maos = ""
        
        if "Close-up" in estilo_cena:
            ref_image_name = "aline rosto.jpeg"
        else:
            ref_image_name = "aline corpo.jpeg"

        outfit = st.text_input(
            "👗 Vestuário da Aline:",
            value="Vestido preto justo de alça fina",
            help="(i) Descreva a roupa que a modelo Aline estará vestindo durante a cena."
        )

    acao_video = st.text_input(
        "✨ Ação Principal no Vídeo:",
        placeholder="Ex: Segurando perto do rosto, mostrando o tecido, virando o produto...",
        help="(i) Descreva o movimento principal que acontecerá no vídeo sem fala."
    )

# ==========================================
# COLUNA DIREITA: OUTPUT E SIMULADOR 9:16
# ==========================================
with col_right:
    st.subheader("📋 Output do Prompt")

    # Montagem do Prompt Final
    if "Visão POV" in estilo_cena:
        prompt_parts = [
            "POV first-person aesthetic video clip, 9:16 vertical video format.",
            f"Top-down POV camera view showing only a woman's hands featuring {detalhes_maos.lower()}.",
            f"The background is set on a {cenario_pov.lower()}."
        ]
        if com_embalagem:
            prompt_parts.append(f"Her hands are opening a clear transparent plastic package/polybag and taking out a {produto_nome if produto_nome else 'product'}.")
        else:
            prompt_parts.append(f"Her hands are gracefully displaying, touching, and holding a {produto_nome if produto_nome else 'product'}.")
            
        if acao_video:
            prompt_parts.append(f"Action: {acao_video}.")
            
        prompt_parts.append("Soft natural window lighting, clean viral aesthetic, ultra high resolution, sharp focus on product and hands.")
    else:
        base_desc = f"Realistic vertical 9:16 video clip based on image reference '{ref_image_name}'. Featuring 'Aline', wearing {outfit}."
        prompt_parts = [
            base_desc,
            f"She is holding and presenting a {produto_nome if produto_nome else 'product'} directly to the camera.",
            f"Action: {acao_video if acao_video else 'smiling gently and showcasing the product without speaking'}.",
            "High resolution, sharp product focus, natural skin texture, soft indoor lighting."
        ]

    prompt_final = " ".join(prompt_parts)

    st.markdown("**1. Imagem de Referência no GitHub:**")
    st.code(ref_image_name, language="text")

    st.markdown("**2. Prompt Otimizado (Pronto para Copiar):**")
    st.code(prompt_final, language="markdown")

    st.markdown("---")
    st.subheader("📱 Simulador de Tela (TikTok / Reels 9:16)")

    # Simulador Visual
    prod_display = produto_nome if produto_nome else "Produto em Destaque"
    acao_display = acao_video if acao_video else "Demonstração do Produto"
    
    st.markdown(
        f"""
        <div class="phone-wrapper">
            <div class="tiktok-card">
                <div class="tiktok-badge">PREVIEW 9:16</div>
                
                <div style="position: absolute; top: 40%; left: 10%; right: 10%; text-align: center;">
                    <p style="font-size: 28px; margin-bottom: 5px;">🎬</p>
                    <p class="tiktok-text" style="font-weight: bold; color: #38BDF8 !important;">{"VISÃO POV (MÃOS)" if "POV" in estilo_cena else "MODELO ALINE"}</p>
                    <p class="tiktok-text" style="font-size: 10px !important; color: #9CA3AF !important;">Foco: {prod_display}</p>
                </div>

                <!-- Botoes Laterais do TikTok -->
                <div class="tiktok-sidebar">
                    <div class="tiktok-icon-btn">❤️</div>
                    <div class="tiktok-icon-btn">💬</div>
                    <div class="tiktok-icon-btn">🔖</div>
                    <div class="tiktok-icon-btn">↪️</div>
                </div>

                <!-- Legenda e Tag do Produto -->
                <div class="tiktok-bottom">
                    <div class="shop-tag">🛒 Loja • Compre Aqui</div>
                    <p class="tiktok-text" style="font-weight: bold;">@aline.studio</p>
                    <p class="tiktok-text" style="font-size: 10px !important;">Ação: {acao_display}</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
