def criar_tarefa(assunto, energia, modo):
    tarefas = {
        "Aprender": {
            "Baixa": f"Leia um tópico sobre {assunto} e anote uma ideia importante.",
            "Média": f"Estude um conceito sobre {assunto} e explique com um exemplo seu.",
            "Alta": f"Estude dois conceitos sobre {assunto} e explique a relação entre eles.",
        },
        "Praticar": {
            "Baixa": f"Resolva um exercício simples sobre {assunto}, consultando um exemplo se precisar.",
            "Média": f"Resolva um exercício sobre {assunto} e explique como chegou à resposta.",
            "Alta": f"Resolva dois exercícios sobre {assunto} e compare suas soluções. Anote o que aprendeu com as diferenças e identifique qual passo foi mais difícil.",
        },
        "Revisar": {
            "Baixa": f"Escolha um tópico da última sessão sobre {assunto} e explique para si, com suas palavras. Anote uma frase do que lembrou.",
            "Média": f"Explique um tópico sobre {assunto} sem consultar o material. Depois confira e corrija uma lacuna.",
            "Alta": f"Crie três perguntas sobre {assunto}, responda sem consultar e confira as respostas no material.",
        },
    }
    return tarefas[modo][energia]
