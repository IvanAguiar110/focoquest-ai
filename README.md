# FocoQuest AI

**Um assunto. Uma missão. Um passo de cada vez.**

Aplicativo de estudos em Python e Streamlit pensado para pessoas com TDAH. A proposta é ajudar a começar uma sessão com uma tarefa curta, um objetivo claro e uma divisão de tempo compatível com a energia disponível.

O projeto está em desenvolvimento e também faz parte do meu aprendizado de Python, organização de código, Git e desenvolvimento de aplicações.

## Estado atual

Este é um protótipo funcional com **missões simuladas por regras em Python**. Apesar do nome FocoQuest AI, ainda não há integração com IA.

O assunto digitado é inserido em frases prontas. O aplicativo não interpreta o tema nem gera conteúdo didático específico sobre ele nesta versão.

## Funcionalidades

- Entrada livre do assunto de estudo.
- Sessões de **15, 25 ou 45 minutos**, com os ritmos Sprint curto, Foco equilibrado e Foco profundo.
- Modos **Aprender, Praticar e Revisar**, com um objetivo para cada modo.
- Tarefa principal ajustada à energia: **baixa, média ou alta**, em cada modo.
- Missão organizada em preparação, exploração e encerramento.
- Desafio extra opcional.
- Botão **Concluir missão**, com confirmação e bloqueio de cliques repetidos.
- Missão mantida entre interações na mesma sessão; gerar outra reinicia a conclusão.
- Aviso quando o assunto está vazio ou contém apenas espaços.

| Modo | Exemplo de tarefa com energia baixa | Objetivo |
| --- | --- | --- |
| Aprender | Ler um tópico e anotar uma ideia | Entender uma ideia nova |
| Praticar | Resolver um exercício simples com apoio de um exemplo | Aplicar o que estudou |
| Revisar | Explicar para si um tópico da última sessão | Recuperar o que estudou e identificar dúvidas |

### Limitações

- A duração divide o tempo em 2 minutos de preparação, o restante para exploração e 3 minutos de encerramento. Não há cronômetro.
- Não há histórico persistente, banco de dados, autenticação ou API REST.
- A missão e sua conclusão ficam apenas na sessão atual. Recarregar a página ou iniciar uma nova sessão reinicia esses dados; não há histórico de missões concluídas.

## Executar localmente

Dependência atual: **Streamlit 1.63.0**. Ambiente usado no desenvolvimento: **Python 3.14.6**.

Os comandos abaixo são para macOS/Linux. Caso ainda não tenha o projeto:

```bash
git clone https://github.com/IvanAguiar110/focoquest-ai.git
cd focoquest-ai
```

Se já possui o projeto, abra o terminal na pasta que contém `app.py` e `missoes.py`.

Na primeira execução, crie o ambiente virtual e instale a dependência:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Inicie o aplicativo:

```bash
python -m streamlit run app.py
```

Abra [http://localhost:8501](http://localhost:8501) no navegador. Esse endereço funciona no computador que está executando o aplicativo. Para encerrar o servidor, pressione `Ctrl+C` no terminal.

Nas próximas sessões, basta entrar na pasta do projeto, ativar o ambiente e iniciar o aplicativo:

```bash
source .venv/bin/activate
python -m streamlit run app.py
```

## Experimentar

1. Digite `variáveis em Python`, escolha 15 minutos e energia Baixa.
2. Clique em **Gerar missão** e confira a tarefa e o objetivo.
3. Gere novamente com energia Média e depois Alta para comparar as sugestões.
   Experimente também Praticar e Revisar: a tarefa e o objetivo devem acompanhar o modo escolhido.
4. Escolha 25 ou 45 minutos e confira o ritmo e o tempo de exploração.
5. Marque **Quero um desafio extra** e gere outra missão.
6. Tente gerar com o assunto vazio ou apenas com espaços: deve aparecer um aviso.
7. Clique em **Concluir missão**: a missão deve continuar visível, com confirmação e botão desabilitado.
8. Gere outra missão: o botão deve ficar disponível novamente. Uma tentativa com assunto vazio deve preservar a missão anterior.

## Organização do código

```text
FocoQuestAI/
├── app.py            # Interface, formulário e estado da missão na sessão
├── missoes.py        # Função criar_tarefa e regras por modo e energia
├── requirements.txt  # Dependência do aplicativo
├── .gitignore        # Arquivos locais excluídos do Git
└── README.md         # Apresentação e instruções
```

`app.py` importa `criar_tarefa` de `missoes.py`. A função recebe o assunto, a energia e o modo e devolve o texto da tarefa principal. O dicionário `tarefas` organiza as frases por modo e, dentro de cada modo, por energia: `tarefas[modo][energia]`. Essa separação permite usar a regra sem abrir a interface do Streamlit.

Com o ambiente virtual ativado, é possível experimentar a função diretamente no terminal:

```bash
python -c 'from missoes import criar_tarefa; print(criar_tarefa("Python", "Baixa", "Aprender"))'
```

Resultado esperado:

```text
Leia um tópico sobre Python e anote uma ideia importante.
```

Os conceitos praticados incluem funções, parâmetros, `return`, módulos e `import`, condições, dicionários e f-strings. O histórico do Git registra a evolução em pequenas etapas.

`st.session_state["missao"]` guarda as escolhas enviadas e o campo booleano `concluida`. O botão de conclusão chama `concluir_missao`, que muda esse campo de `False` para `True`. A exibição lê a missão guardada, sem depender de um novo clique em **Gerar missão**.

## Próximos passos

- Publicar uma demonstração que possa ser acessada pelo navegador.
- Experimentar uma API REST com FastAPI reutilizando as regras de estudo.
- Integrar IA para produzir missões específicas, com proteção da chave e controle de custos.

Esses itens são planos de evolução; ainda não estão implementados.
