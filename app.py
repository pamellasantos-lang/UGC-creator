import streamlit as st

# 1. Configuração da página em Modo Wide
st.set_page_config(
    page_title="UGC Ad Studio - Gerador Modular",
    page_icon="🎬",
    layout="wide"
)

# 2. Estilização CSS de Alta Visibilidade (Estúdio Claro Pro & Alto Contraste)
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
st.caption("Crie prompts otimizados em português com suporte a transições virais, CTA visual e cenas de continuidade.")

st.markdown("---")

col_left, col_mid, col_right = st.columns([1, 1.1, 1], gap="medium")

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
# COLUNA 2: CENÁRIO, AÇÕES E CTA VISUAL
# ==========================================
with col_mid:
    st.subheader("⚡ Cenário & CTA Visual")

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
    st.write("**🛒 Chamada para Ação (CTA Visual)**")
    
    cta_choice = st.radio(
        "Selecione o Texto da Chamada para Ação:",
        ["Compre Aqui 👇", "Saiba Mais 👇", "Garanta o Seu 👇"],
        horizontal=True,
        help="(i) O prompt enviará um comando para a IA fazer a personagem/mãos apontarem para baixo no final do vídeo."
    )

    gerar_continuidade = st.checkbox(
        "Gerar Prompt da Cena 2 (Continuidade para mostrar mais detalhes)",
        value=True,
        help="(i) Cria um segundo comando focado em aproximar a câmera e exibir o produto com mais tempo de tela."
    )

# ==========================================
# COLUNA 3: OUTPUT DE PROMPTS (CENA 1 E CENA 2)
# ==========================================
with col_right:
    st.subheader("📋 Output dos Prompts")

    # Comando visual explicito de CTA para apontar para baixo
    cta_prompt_visual = (
        f"Nos últimos 2 segundos do vídeo, a cena traz um elemento visual e um gesto direto apontando claramente para a parte inferior central da tela "
        f"(apontando para baixo em direção ao carrinho/botão de compra) com uma seta indicativa e legenda visível dizendo '{cta_choice}'."
    )

    # --- CENA 1 / PROMPT PRINCIPAL ---
    prompt_cena1 = []
    if "Foto" in tipo_midia:
        prompt_cena1.append("Fotografia comercial de produto em alta resolução, proporção vertical 9:16.")
    else:
        prompt_cena1.append("Vídeo clipe vertical 9:16 ultra-realista no estilo UGC viral do TikTok.")

    # Ritmo de Câmera
    if "Câmera Lenta" in ritmo_duracao:
        prompt_cena1.append("Movimento de câmera e ação em câmera lenta (slow motion 0.5x), tempo estendido e ritmado suavemente.")
    elif "Suave" in ritmo_duracao:
        prompt_cena1.append("Movimento de câmera suave, fluidez contínua e pausada.")

    # Lógica de Construção por Perspectiva
    if "Transição Viral" in tipo_plano:
        prompt_cena1.append(f"PARTE 1: Perspectiva em primeira pessoa (POV) vista de cima das {detalhes_membro.lower()} rasgando a embalagem plástica transparente com calma, retirando o(a) {produto_nome if produto_nome else 'produto'} de dentro e arrumando a peça sobre {cenario.lower()}, exatamente como mostrado na foto de referência.")
        prompt_cena1.append(f"TRANSIÇÃO CORTE RÁPIDO (JUMP CUT): A modelo da foto de referência aparece vestindo o(a) mesmo(a) {produto_nome if produto_nome else 'produto'}, gravando um vídeo de selfie no espelho de corpo inteiro com seu smartphone no quarto. Ela se vira suavemente mostrando o caimento do produto e o ajuste no corpo.")

    elif "Showcase" in tipo_plano:
        prompt_cena1.append("Movimento dinâmico de câmera em 360 graus girando lentamente ao redor do modelo.")
        if tipo_peca:
            prompt_cena1.append(f"Apresentando o(a) {produto_nome if produto_nome else 'produto'}.")
        prompt_cena1.append(f"Apresentando a personagem vestindo {detalhes_membro.lower()}.")

    elif "POV" in tipo_plano:
        prompt_cena1.append("Perspectiva em primeira pessoa (POV) vista de cima em ritmo lento.")
        prompt_cena1.append(f"Apresentando {detalhes_membro.lower()} interagindo diretamente com a peça.")
        
        if embalagem_efeito:
            prompt_cena1.append(f"Ação de Unboxing em movimento pausado: As mãos rasgam a embalagem plástica transparente com calma, retiram o(a) {produto_nome if produto_nome else 'produto'} de dentro e o(a) posicionam cuidadosamente sobre {cenario.lower()}, estendendo o produto exatamente como mostrado na foto de referência.")
        else:
            prompt_cena1.append(f"Ação: {acao_dinamica if acao_dinamica else 'exibindo e tocando o produto suavemente'}.")

    else:
        prompt_cena1.append(f"Apresentando a personagem da imagem de referência vestindo {detalhes_membro.lower()}.")
        if embalagem_efeito:
            prompt_cena1.append(f"Ação de Unboxing: As mãos rasgam a embalagem plástica transparente com calma, retiram o(a) {produto_nome if produto_nome else 'produto'} de dentro e o(a) posicionam sobre {cenario.lower()}, exatamente como na foto de referência.")
        elif acao_dinamica:
            prompt_cena1.append(f"Ação: {acao_dinamica}.")

    # Inclusão da CTA no final
    prompt_cena1.append(cta_prompt_visual)
    prompt_cena1.append(f"Cenário: {cenario.lower()}. {iluminacao}, foco nítido no produto, ultra alta resolução, estética comercial limpa estilo UGC.")
    prompt_final_1 = " ".join(prompt_cena1)

    st.markdown("**1. Prompt Principal (Cena 1 / Com CTA Apontando para Baixo):**")
    st.code(prompt_final_1, language="markdown")

    # --- CENA 2 (CONTINUIDADE E DETALHES DO PRODUTO) ---
    if gerar_continuidade:
        prompt_cena2 = [
            "Continuação da cena em vídeo clipe vertical 9:16 em câmera lenta.",
            f"Plano aproximado (Close-up em slow motion) com foco total nos detalhes do(a) {produto_nome if produto_nome else 'produto'} já posicionado(a) sobre {cenario.lower()}.",
            f"{detalhes_membro.title()} passam a mão suavemente sobre o tecido e textura do produto, virando levemente a peça para mostrar os acabamentos, costuras e detalhes de perto.",
            cta_prompt_visual,
            "Panorâmica lenta de câmera deslizando sobre o produto. Foco nítido, iluminação natural de estúdio, estética comercial detalhada."
        ]
        prompt_final_2 = " ".join(prompt_cena2)

        st.markdown("**2. Prompt - Cena 2 (Continuidade & Detalhes + CTA Final):**")
        st.code(prompt_final_2, language="markdown")

    # Dica Técnica
    st.info("💡 **Dica do CTA:** O comando agora inclui uma instrução explícita de gesto/indicação visual com a mensagem 'Compre Aqui 👇' apontando para a borda inferior, que é onde fica o carrinho de compras nos anúncios do TikTok e Reels.")

    st.markdown("---")
    st.markdown("**Simulador de Tela (TikTok 9:16)**")

    st.markdown(
        f"""
        <div class="phone-wrapper">
            <div class="tiktok-card">
                <div class="tiktok-badge">PREVIEW 9:16</div>
                <div style="position: absolute; top: 38%; left: 10%; right: 10%; text-align: center;">
                    <p style="font-size: 26px; margin-bottom: 5px;">{"👇"}</p>
                    <p class="tiktok-text" style="font-weight: bold; color: #38BDF8 !important;">{cta_choice.upper()}</p>
                    <p class="tiktok-text" style="font-size: 10px !important; color: #9CA3AF !important;">{produto_nome if produto_nome else 'Produto'}</p>
                </div>
                <div class="tiktok-sidebar">
                    <div class="tiktok-icon-btn">❤️</div>
                    <div class="tiktok-icon-btn">💬</div>
                    <div class="tiktok-icon-btn">🔖</div>
                </div>
                <div class="tiktok-bottom">
                    <div class="shop-tag">🛒 {cta_choice}</div>
                    <p class="tiktok-text" style="font-weight: bold;">@ugc.studio</p>
                    <p class="tiktok-text" style="font-size: 10px !important; color: #D1D5DB !important;">Foco: {ritmo_duracao.split('/')[0]}</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
