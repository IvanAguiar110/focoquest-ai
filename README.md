# FocoQuest AI

Aplicativo de estudos em Python pensado para pessoas com TDAH.
Nesta primeira sessão, temos uma tela em Streamlit com missões simuladas.

## Executar

Ambiente verificado: Python 3.14.6. Na pasta do projeto:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Se o ambiente já estiver instalado, use apenas os comandos de ativação e execução.
Abra http://localhost:8501. Para encerrar, pressione `Ctrl+C` no terminal.

## Experimentar

1. Informe um assunto, escolha 15, 25 ou 45 minutos e sua energia.
2. Clique em **Gerar missão**. A tarefa muda conforme a energia.
3. Tente gerar com o assunto vazio: o aplicativo deve pedir um assunto.

A duração é uma sugestão de divisão do tempo; não há cronômetro nesta versão.
As missões usam textos locais, sem API de IA, banco de dados ou autenticação.

## Entender o código

Tudo acontece em `app.py`:

- **Variável:** `tarefa_baixa = "..."` guarda a frase escrita por você.
- **Condição:** `if` / `elif` / `else` escolhem a tarefa conforme a energia.
- **Exibição:** `st.write(tarefa)` mostra o texto escolhido na tela.

`requirements.txt` registra a versão do Streamlit.
`.gitignore` mantém o ambiente virtual e arquivos locais fora dos commits.
Um commit é um ponto salvo no histórico do projeto.

Referência: [instalação do Streamlit](https://docs.streamlit.io/get-started/installation/command-line).
