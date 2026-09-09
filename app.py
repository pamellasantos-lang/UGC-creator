import os
import streamlit as st
from PIL import Image

# Configuração da Página
st.set_page_config(
    page_title="UGC Studio - Aline",
    page_icon="🎬",
    layout="wide"
)

# Estilização CSS com Alto Contraste (Garantindo leitura perfeita de textos, campos e placeholders)
st.markdown("""
    <style>
    /* Fundo Escuro Limpo */
    .stApp {
        background-color: #0E1117;
        color: #F0F6FC;
    }

    /* Labels e Textos Principais */
    label, p, h1, h2, h3, h4, span {
        color: #F0F6FC !important;
        font-weight: 500;
    }

    /* Campos de Entrada (Inputs) */
    .stTextInput input, .stSelectbox div[data-baseweb="select"] {
        background-color: #161B22 !important;
        color: #FFFFFF !important;
        border: 1px solid #30363D !important;
        border-radius: 6px !important;
    }

    /* Cor do Placeholder (Texto Exemplo de Fundo) */
    .stTextInput input::placeholder {
        color: #8B949E !important;
        opacity: 1 !important;
    }

    /* Bloco de Código do Prompt - Corrigindo Fundo e Cor da Letra */
    div[data-testid="stCodeBlock"] pre {
        background-color: #161B22 !important;
        border: 1px solid #30363D !important;
        border-radius: 8px !important;
    }
    div[data-testid="stCodeBlock"] code {
        color: #58A6FF !important; /* Azul brilhante de alto contraste */
        font-family: 'Courier New', Courier, monospace !important;
        font-size: 14px !important;
    }

    /* Card de Preview Visual */
    .preview-card {
        background-color: #161B22;
        border: 1px solid #30363D;
        border-radius: 10px;
        padding: 16px;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Título
st.title("🎬 UGC Studio - Aline")
st.caption("Gerador de Prompts e Prévia Visual para Conteúdos no TikTok / Reels.")

st.markdown("---")

col_left, col_right = st.columns([1, 1], gap="large")

# ==========================================
# COLUNA ESQUERDA: CONFIGURAÇÃO DOS CAMPOS
# ==========================================
with col_left:
    st.subheader("⚙️ Parâmetros do Vídeo")

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
        ref_image_name = None
        
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
# COLUNA DIREITA: OUTPUT E PREVIA VISUAL
# ==========================================
with col_right:
    st.subheader("📋 Output do Prompt")

    # Construção do Prompt
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
    st.code(ref_image_name if ref_image_name else "Nenhuma (Visão POV - Sem Rosto)", language="text")

    st.markdown("**2. Prompt Gerado (Para Kling AI / Luma / Runway):**")
    st.code(prompt_final, language="markdown")

    st.markdown("---")
    st.subheader("🖼️ Prévia Visual da Cena")

    # Exibição de Imagem ou Mockup Visual de Prévia
    if ref_image_name and os.path.exists(ref_image_name):
        image = Image.open(ref_image_name)
        st.image(image, caption=f"Imagem Base: {ref_image_name}", use_column_width=True)
    else:
        st.markdown(
            f"""
            <div class="preview-card">
                <p style="color: #58A6FF; font-weight: bold; margin-bottom: 8px;">ESTRUTURA DA CENA PREVISTA (9:16)</p>
                <ul>
                    <li><b>Enquadramento:</b> {"Visão Primeira Pessoa (POV)" if "POV" in estilo_cena else "Modelo Físico (Aline)"}</li>
                    <li><b>Elemento Principal:</b> {produto_nome if produto_nome else "Produto não informado"}</li>
                    <li><b>Ambiente:</b> {cenario_pov if "POV" in estilo_cena else "Quarto/Ambiente Interno"}</li>
                    <li><b>Efeito de Unboxing:</b> {"Ativado (Embalagem Plástica)" if com_embalagem else "Desativado"}</li>
                    <li><b>Detalhes Visuais:</b> {detalhes_maos if "POV" in estilo_cena else outfit}</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
