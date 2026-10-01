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
- Tarefa principal e objetivo conforme a energia: **baixa, média ou alta**.
- Missão organizada em preparação, exploração e encerramento.
- Desafio extra opcional.
- Aviso quando o assunto está vazio ou contém apenas espaços.

| Energia | Tarefa sugerida | Objetivo |
| --- | --- | --- |
| Baixa | Ler um tópico e anotar uma ideia | Entender uma ideia principal |
| Média | Estudar um conceito e explicar com um exemplo | Explicar o tema com um exemplo |
| Alta | Resolver um exercício e explicar a resposta | Aplicar o tema em um exercício |

### Limitações

- O campo **“Como quero estudar”** oferece Aprender, Praticar e Revisar, mas ainda não influencia a missão.
- A duração divide o tempo em 2 minutos de preparação, o restante para exploração e 3 minutos de encerramento. Não há cronômetro.
- Não há histórico persistente, banco de dados, autenticação ou API REST.
- A missão é exibida após o envio do formulário; não há acompanhamento de conclusão nesta versão.

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
4. Escolha 25 ou 45 minutos e confira o ritmo e o tempo de exploração.
5. Marque **Quero um desafio extra** e gere outra missão.
6. Tente gerar com o assunto vazio ou apenas com espaços: deve aparecer um aviso.

## Organização do código

```text
FocoQuestAI/
├── app.py            # Interface, formulário e exibição da missão
├── missoes.py        # Função criar_tarefa e regras por energia
├── requirements.txt  # Dependência do aplicativo
├── .gitignore        # Arquivos locais excluídos do Git
└── README.md         # Apresentação e instruções
```

`app.py` importa `criar_tarefa` de `missoes.py`. A função recebe o assunto e a energia e devolve o texto da tarefa principal. Essa separação permite usar a regra sem abrir a interface do Streamlit.

Com o ambiente virtual ativado, é possível experimentar a função diretamente no terminal:

```bash
python -c 'from missoes import criar_tarefa; print(criar_tarefa("Python", "Baixa"))'
```

Resultado esperado:

```text
Leia um tópico sobre Python e anote uma ideia importante.
```

Os conceitos praticados incluem funções, parâmetros, `return`, módulos e `import`, condições, dicionários e f-strings. O histórico do Git registra a evolução em pequenas etapas.

## Próximos passos

- Conectar o modo de estudo à geração da tarefa.
- Publicar uma demonstração que possa ser acessada pelo navegador.
- Experimentar uma API REST com FastAPI reutilizando as regras de estudo.
- Integrar IA para produzir missões específicas, com proteção da chave e controle de custos.

Esses itens são planos de evolução; ainda não estão implementados.
