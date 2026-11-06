import streamlit as st

from missoes import criar_tarefa

st.set_page_config(page_title="FocoQuest AI", page_icon="🎯", layout="centered")

# Inicializa apenas uma vez; preserva a missão entre os cliques desta sessão.
if "missao" not in st.session_state:
    st.session_state["missao"] = None


def concluir_missao():
    st.session_state["missao"]["concluida"] = True


st.title("🎯 FocoQuest AI")
st.write("Um assunto. Uma missão. Um passo de cada vez.")
st.caption("Escolha o que cabe na sua energia de hoje.")

# O formulário envia as escolhas quando você clica no botão.
with st.form("nova_missao"):
    assunto = st.text_input("Assunto que quero estudar", placeholder="Ex.: variáveis em Python")
    duracao = st.selectbox("Duração (minutos)", [15, 25, 45])
    modo = st.selectbox("Como quero estudar", ["Aprender", "Praticar", "Revisar"])
    energia = st.radio("Energia", ["Baixa", "Média", "Alta"], horizontal=True)
    desafio_extra = st.checkbox("Quero um desafio extra")
    gerar_missao = st.form_submit_button("Gerar missão", type="primary")

if gerar_missao:
    # strip() retira espaços das pontas, para validar também uma entrada só com espaços.
    assunto = assunto.strip()

    if not assunto:
        st.warning("Escreva um assunto para começar. Pode ser algo pequeno.")
    else:
        # Guarda as escolhas enviadas, separadas das próximas edições do formulário.
        st.session_state["missao"] = {
            "assunto": assunto,
            "duracao": duracao,
            "modo": modo,
            "energia": energia,
            "desafio_extra": desafio_extra,
            "tarefa": criar_tarefa(assunto, energia, modo),
            "concluida": False,
        }

# Exibe a missão guardada mesmo quando o clique foi em outro botão.
missao = st.session_state["missao"]
if missao is not None:
    minutos_de_foco = missao["duracao"] - 5
    ritmos = {
        15: "Sprint curto",
        25: "Foco equilibrado",
        45: "Foco profundo",
    }
    objetivos = {
        "Aprender": "Entender uma ideia nova sobre o tema.",
        "Praticar": "Aplicar o que estudou em um exercício.",
        "Revisar": "Recuperar o que estudou e identificar dúvidas.",
    }

    ritmo = ritmos[missao["duracao"]]
    objetivo = objetivos[missao["modo"]]
    with st.container(border=True):
        st.subheader("Sua missão")
        if missao["concluida"]:
            st.success("Missão concluída! Você conseguiu mais um progresso em seu estudo.")
        else:
            st.success("Missão criada. Comece pelo primeiro passo.")
        st.text(f"Assunto: {missao['assunto']}")
        st.caption(
            f"{missao['duracao']} minutos · {ritmo} · Energia {missao['energia'].lower()} · "
            f"Modo {missao['modo'].lower()} · Missão simulada"
        )
        st.info(f"Objetivo: {objetivo}")
        st.markdown("**1. Prepare · 2 min**")
        st.write("Abra um material sobre o assunto e escolha um trecho pequeno.")
        st.markdown(f"**2. Explore · {minutos_de_foco} min**")
        st.write(missao["tarefa"])
        st.markdown("**3. Feche · 3 min**")
        st.write("Releia sua anotação e registre uma dúvida para a próxima sessão.")
        if missao["desafio_extra"]:
            st.markdown("**⭐ Desafio extra**")
            st.write("Explique o tema sem consultar o material.")
        st.button(
            "Concluir missão",
            on_click=concluir_missao,
            disabled=missao["concluida"],
        )
    st.caption("A missão é temporária: recarregar a página reinicia a sessão.")
else:
    st.info("Sua missão aparecerá aqui depois de clicar em Gerar missão.")
