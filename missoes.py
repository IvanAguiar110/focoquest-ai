def criar_tarefa(assunto, energia):
    if energia == "Baixa":
        return f"Leia um tópico sobre {assunto} e anote uma ideia importante."
    elif energia == "Média":
        return f"Estude um conceito sobre {assunto} e explique com um exemplo seu."
    else:
        return f"Resolva um exercício sobre {assunto} e explique como chegou à resposta."