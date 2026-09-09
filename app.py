import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="UGC Studio - Aline",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização CSS de Alto Contraste (Textos claros sobre fundo escuro limpo)
st.markdown("""
    <style>
    /* Fundo da aplicação */
    .stApp {
        background-color: #0E1117;
        color: #F0F6FC;
    }
    
    /* Garantir alto contraste nos rótulos de texto */
    label, .stMarkdown, p, h1, h2, h3, h4, span {
        color: #F0F6FC !important;
    }

    /* Inputs, Selectboxes e Caixas de texto com fundo escuro e texto branco */
    .stTextInput input, .stSelectbox select, .stTextArea textarea {
        background-color: #161B22 !important;
        color: #FFFFFF !important;
        border: 1px solid #30363D !important;
        border-radius: 8px !important;
    }

    /* Ajuste de cor em botões do Radio e Checkbox */
    .stRadio div, .stCheckbox div {
        color: #F0F6FC !important;
    }

    /* Cards e Caixas de destaque */
    .stAlert {
        background-color: #161B22 !important;
        color: #F0F6FC !important;
        border: 1px solid #30363D !important;
    }

    /* Badge de destaque */
    .badge-aline {
        background-color: #238636;
        color: #FFFFFF !important;
        padding: 6px 14px;
        border-radius: 12px;
        font-size: 13px;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# Header Principal
st.markdown("<span class='badge-aline'>MODELO FIXA: ALINE</span>", unsafe_allow_html=True)
st.title("🎬 UGC Studio - Aline")
st.caption("Central de geração de prompts de alta conversão para produtos no TikTok & Reels.")

st.markdown("---")

# Layout em Duas Colunas Organizadoras
col_config, col_output = st.columns([1.1, 1], gap="large")

with col_config:
    st.subheader("⚙️ Configurações da Cena")
    
    # Seleção do Estilo do Vídeo
    estilo_cena = st.selectbox(
        "🎥 Selecione o Estilo do Vídeo:",
        [
            "Visão POV - Mãos & Unboxing (Apenas mãos com joias e unhas decoradas)",
            "Close-up de Rosto (Aline segurando produto ao lado do rosto)",
            "Corpo Inteiro Lifestyle (Aline mostrando o produto no quarto)",
            "Selfie no Espelho (Aline mostrando produto / look inteiro)"
        ]
    )

    # Seleção de Imagem de Referência do GitHub
    if "Visão POV" in estilo_cena:
        ref_image = "Nenhuma (Visão POV - Foco Apenas nas Mãos)"
        st.info("💡 Modo POV selecionado: A IA vai gerar o foco nas mãos com fundo estético, sem necessidade do rosto.")
    elif "Close-up" in estilo_cena:
        ref_image = "aline rosto.jpeg"
        st.success("📁 Referência do GitHub ativada: **aline rosto.jpeg**")
    else:
        ref_image = "aline corpo.jpeg"
        st.success("📁 Referência do GitHub ativada: **aline corpo.jpeg**")

    # Informações do Produto
    produto_nome = st.text_input("📦 Nome / Descrição do Produto:", placeholder="Ex: Camiseta amarela, Conjunto de pijama de coração, Sérum facial...")

    # Opções específicas para cada tipo de vídeo
    if "Visão POV" in estilo_cena:
        com_embalagem = st.checkbox("📦 Efeito Unboxing (Tirando o produto de dentro do saco plástico transparente)", value=True)
        cenario_pov = st.selectbox(
            "🛏️ Cenário de Fundo (POV):",
            [
                "Cama com edredom neutro e tapete felpudo branco",
                "Chão de madeira clara com tapete felpudo branco (estilo TikTok)",
                "Mesa minimalista de mármore com iluminação natural"
            ]
        )
        detalhes_maos = st.text_input(
            "💅 Detalhes das Mãos & Acessórios:", 
            value="Mãos com unhas compridas bem pintadas e decoradas, usando anéis delicados, pulseira e relógio"
        )
        outfit = ""
    else:
        com_embalagem = False
        cenario_pov = ""
        detalhes_maos = ""
        outfit = st.text_input("👗 Vestuário da Aline:", value="Vestido preto justo de alça fina (conforme foto de referência)")

    acao_video = st.text_input("✨ Ação Principal com o Produto:", placeholder="Ex: Mostrando o tecido, dobrando a peça, passando a mão levemente sobre o produto...")

with col_output:
    st.subheader("📋 Output do Prompt")
    
    # Construção Inteligente do Prompt
    if "Visão POV" in estilo_cena:
        prompt_parts = [
            "POV first-person aesthetic video clip, 9:16 vertical video format.",
            f"Top-down POV camera view showing only a woman's hands featuring {detalhes_maos.lower()}.",
            f"The background is set on a {cenario_pov.lower()}."
        ]
        if com_embalagem:
            prompt_parts.append(f"Her hands are opening a clear transparent plastic package/polybag and taking out a {produto_nome}.")
        else:
            prompt_parts.append(f"Her hands are gracefully displaying, touching, and holding a {produto_nome}.")
            
        if acao_video:
            prompt_parts.append(f"Action: {acao_video}.")
            
        prompt_parts.append("Soft natural window lighting, clean viral aesthetic, ultra high resolution, sharp focus on product and hands.")
    else:
        if ref_image == "aline rosto.jpeg":
            base_desc = f"Realistic vertical 9:16 video clip based on image reference 'aline rosto.jpeg'. Featuring 'Aline', a young Latina woman with long dark brown hair, warm tan skin, glossy nude lips, wearing a gold chain necklace and small gold hoop earrings."
        else:
            base_desc = f"Full-body realistic 9:16 video clip based on image reference 'aline corpo.jpeg'. Featuring 'Aline', wearing {outfit}, standing in a bright modern bedroom."
        
        prompt_parts = [
            base_desc,
            f"She is holding and presenting a {produto_nome} directly to the camera.",
            f"Action: {acao_video if acao_video else 'smiling gently and showcasing the product features without speaking'}.",
            "High resolution, sharp product focus, natural skin texture, soft indoor lighting."
        ]

    prompt_final = " ".join(prompt_parts)

    st.markdown("**1. Imagem de Referência no GitHub:**")
    st.code(ref_image, language="text")

    st.markdown("**2. Prompt Otimizado para IA de Vídeo (Kling / Luma / Runway):**")
    st.code(prompt_final, language="markdown")

    st.markdown("---")
    st.markdown("### 💡 Como Usar na Ferramenta de Vídeo")
    if "Visão POV" in estilo_cena:
        st.markdown("* Para vídeos **POV**, cole diretamente o prompt acima no gerador de texto-para-vídeo. A IA gerará a composição das mãos com o produto no cenário configurado.")
    else:
        st.markdown(f"* Baixe a foto **`{ref_image}`** do seu GitHub e insira como imagem inicial (Image-to-Video) na ferramenta de IA junto com o prompt gerado.")
