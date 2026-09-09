# Adicione no dropdown de 'Perspectiva / Estilo da Câmera':
tipo_plano = st.selectbox(
    "Perspectiva / Estilo da Câmera:",
    [
        "Transição Viral - Unboxing na Cama ➔ Provador no Espelho (Try-On)",
        "Visão POV (Apenas Mãos em Primeira Pessoa)",
        "Showcase Model - Câmera 360° em Volta (Giro + Zooms de Detalhes da Peça)",
        "Modelo em Cena - Close-up (Rosto / Busto)",
        "Modelo em Cena - Corpo Inteiro (Lifestyle)"
    ]
)

# Lógica de montagem do prompt para a opção de Transição
if "Transição Viral" in tipo_plano:
    prompt_elements = [
        "Vídeo clipe vertical 9:16 ultra-realista no estilo UGC viral do TikTok.",
        f"PARTE 1: Vista POV em primeira pessoa de cima das {detalhes_membro.lower()} rasgando a embalagem plástica transparente, retirando o(a) {produto_nome if produto_nome else 'produto'} e arrumando a peça sobre {cenario.lower()}.",
        f"TRANSIÇÃO CORTE RÁPIDO (JUMP CUT): A modelo da foto de referência aparece vestindo o(a) mesmo(a) {produto_nome if produto_nome else 'produto'}, gravando um vídeo de selfie no espelho de corpo inteiro com seu smartphone.",
        "Ela se vira suavemente mostrando o caimento do produto e o ajuste no corpo. Iluminação natural de janela, foco nítido, alta resolução."
    ]
