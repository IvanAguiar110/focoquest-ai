import streamlit as st

def criar_tarefa(assunto, energia):
    if energia == "Baixa":
        return f"Leia um resumo curto sobre {assunto} e anote uma ideia importante."
    elif energia == "Média":
        return f"Estude um conceito sobre {assunto} e explique com um exemplo seu."
    else:
        return f"Resolva um exercício sobre {assunto} e explique como chegou à resposta."


st.set_page_config(page_title="FocoQuest AI", page_icon="🎯", layout="centered")

st.title("🎯 FocoQuest AI")
st.write("Um assunto. Uma missão. Um passo de cada vez.")
st.caption("Escolha o que cabe na sua energia de hoje.")

# O formulário envia as escolhas quando você clica no botão.
with st.form("nova_missao"):
    assunto = st.text_input("Assunto que quero estudar", placeholder="Ex.: variáveis em Python")
    duracao = st.selectbox("Duração (minutos)", [15, 25, 45])
    energia = st.radio("Energia", ["Baixa", "Média", "Alta"], horizontal=True)
    desafio_extra = st.checkbox("Quero um desafio extra")
    gerar_missao = st.form_submit_button("Gerar missão", type="primary")

if gerar_missao:
    # strip() retira espaços das pontas, para validar também uma entrada só com espaços.
    assunto = assunto.strip()

    if not assunto:
        st.warning("Escreva um assunto para começar. Pode ser algo pequeno.")
    else:
        tarefa = criar_tarefa(assunto, energia)

        # Reservamos 2 minutos para começar e 3 para revisar.
        minutos_de_foco = duracao - 5
        ritmos = {
            15: "Sprint curto",
            25: "Foco equilibrado",
            45: "Foco profundo",
        }
        objetivos = {
            "Baixa": "Entender uma ideia principal.",
            "Média": "Explicar o tema com um exemplo.",
            "Alta": "Aplicar o tema em um exercício.",
        }

        ritmo = ritmos[duracao]
        objetivo = objetivos[energia]
        with st.container(border=True):
            st.subheader("Sua missão")
            st.success("Missão criada. Comece pelo primeiro passo.")
            st.text(f"Assunto: {assunto}")
            st.caption(
                f"{duracao} minutos · {ritmo} · Energia {energia.lower()} · Missão simulada"
                )
            st.info(f"Objetivo: {objetivo}")
            st.markdown("**1. Prepare · 2 min**")
            st.write("Abra um material sobre o assunto e escolha um trecho pequeno.")
            st.markdown(f"**2. Explore · {minutos_de_foco} min**")
            st.write(tarefa)
            st.markdown("**3. Feche · 3 min**")
            st.write("Releia sua anotação e registre uma dúvida para a próxima sessão.")
            if desafio_extra:
                st.markdown("**⭐ Desafio extra**")
                st.write("Explique o tema sem consultar o material.")
else:
    st.info("Sua missão aparecerá aqui depois de clicar em Gerar missão.")
