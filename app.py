import streamlit as st


st.set_page_config(page_title="FocoQuest AI", page_icon="🎯", layout="centered")

st.title("🎯 FocoQuest AI")
st.write("Um assunto. Uma missão. Um passo de cada vez.")
st.caption("Escolha o que cabe na sua energia de hoje.")

# O formulário envia as escolhas quando você clica no botão.
with st.form("nova_missao"):
    assunto = st.text_input("Assunto que quero estudar", placeholder="Ex.: variáveis em Python")
    duracao = st.selectbox("Duração (minutos)", [15, 25, 45])
    energia = st.radio("Energia", ["Baixa", "Média", "Alta"], horizontal=True)
    gerar_missao = st.form_submit_button("Gerar missão", type="primary")

if gerar_missao:
    # strip() retira espaços das pontas, para validar também uma entrada só com espaços.
    assunto = assunto.strip()

    if not assunto:
        st.warning("Escreva um assunto para começar. Pode ser algo pequeno.")
    else:
        # Sua primeira contribuição em Python: uma variável que guarda texto.
        tarefa_baixa = "Leia um resumo curto do tema e dê uma ideia importante."

        if energia == "Baixa":
            tarefa = tarefa_baixa
        elif energia == "Média":
            tarefa = "Estude um conceito do tema e explique com um exemplo seu."
        else:
            tarefa = "Resolva um exercício do tema e explique como chegou à resposta."

        # Reservamos 2 minutos para começar e 3 para revisar.
        minutos_de_foco = duracao - 5

        with st.container(border=True):
            st.subheader("Sua missão")
            st.text(f"Assunto: {assunto}")
            st.caption(f"{duracao} minutos · Energia {energia.lower()} · Missão simulada")
            st.markdown("**1. Prepare · 2 min**")
            st.write("Abra um material sobre o assunto e escolha um trecho pequeno.")
            st.markdown(f"**2. Explore · {minutos_de_foco} min**")
            st.write(tarefa)
            st.markdown("**3. Feche · 3 min**")
            st.write("Releia sua anotação e registre uma dúvida para a próxima sessão.")
else:
    st.info("Sua missão aparecerá aqui depois de clicar em Gerar missão.")
