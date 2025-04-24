#Crie uma lista tarefas = [].
#Use append() para adicionar tarefas: "estudar", "trabalhar", "dormir".
#Use pop() para simular a conclusão da última tarefa e imprima: "Tarefa concluída: [tarefa]"

tarefas = []
tarefas.append("estudar")
tarefas.append("trabalhar")
tarefas.append("dormir")
tarefa_concluida = tarefas.pop()
print(f"Tarefa concluída: {tarefa_concluida}")
