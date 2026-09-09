import streamlit as st

# Configuração da Página
st.set_page_config(page_title="Gerador de Prompts - Aline", page_icon="🎬")

st.title("🎬 Gerador de Prompts UGC - Modelo Aline")
st.write("Preencha os dados do produto para gerar comandos otimizados para Kling AI, Luma ou Runway.")

# 1. Perfil Fixo da Modelo (A nossa "Identidade Core")
aline_profile = (
    "realistic photograph of 'Aline,' a young Latina woman (approx. 24) with long, dark brown hair parted. "
    "She has warm, tan skin, detailed dark eyes with full eyelashes and peach-toned blush/eyeshadow. "
    "Glossy nude lips are her signature. She wears a minimal gold chain necklace and small gold hoop earrings."
)

# 2. Formulário de Entrada do Usuário
with st.form("prompt_form"):
    st.subheader("Configurações do Vídeo")
    
    produto = st.text_input("Qual o produto que ela vai vender?", placeholder="Ex: Sérum Facial de Vitamina C, Fone de Ouvido...")
    
    tipo_video = st.selectbox(
        "Qual o tipo de enquadramento?",
        [
            "Close-up (Demonstração de Rosto/Mão)", 
            "Corpo Inteiro (Lifestyle/Quarto)", 
            "Externa (Rua/Café)"
        ]
    )
    
    cenario = st.text_input("Descreva o cenário rapidamente:", placeholder="Ex: quarto moderno bem iluminado, banheiro luxuoso...")
    
    acao = st.text_input("Qual a ação dela com o produto?", placeholder="Ex: segurando perto do rosto, mostrando para a câmera...")
    
    roupa = st.text_input("Qual a roupa (outfit)?", value="black mini-dress")

    submit_button = st.form_submit_button("Gerar Prompt 🚀")

# 3. Lógica de Geração do Prompt
if submit_button:
    if not produto or not cenario:
        st.warning("Por favor, preencha o produto e o cenário!")
    else:
        st.success("Prompt Gerado com Sucesso! Copie abaixo:")
        
        # Montando o prompt condicionalmente
        if tipo_video == "Close-up (Demonstração de Rosto/Mão)":
            prompt_final = f"A detailed close-up photograph featuring Aline's face. {aline_profile} She is smiling gently. She is {acao} a {produto}. The background is a softly blurred {cenario}. She is wearing a {roupa}. High resolution, precise focus, natural skin texture, 9:16 aspect ratio."
            
        elif tipo_video == "Corpo Inteiro (Lifestyle/Quarto)":
            prompt_final = f"A detailed full-body photograph. {aline_profile} Aline is standing confidently in a {cenario}. She is {acao} a {produto}. She is wearing a {roupa}. High resolution, shallow depth of field, natural soft indoor lighting. Aspect ratio 9:16."
            
        else:
            prompt_final = f"A full-body photograph featuring Aline standing outside in a {cenario}. {aline_profile} She is {acao} a {produto}. She is wearing a {roupa}. Natural daylight, candid lifestyle photography. 9:16 aspect ratio."
        
        # Exibe o código em uma caixa fácil de copiar
        st.code(prompt_final, language='markdown')
        
        st.info("💡 Dica: Cole este texto na sua ferramenta de imagem/vídeo usando as fotos de referência da Aline.")
