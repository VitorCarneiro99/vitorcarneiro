tasks = []

def add_task():
    task = input("Qual é a tarefa que deseja adicionar? ")
    tasks.append(task)
    print("Tarefa adicionada com sucesso!")

def delete_task():
    task = input("Qual é a tarefa que deseja excluir? ")
    if task in tasks:
        tasks.remove(task)
        print("Tarefa removida com sucesso!")
    else:
        print("Tarefa não encontrada na lista.")

def update_task():
    task = input("Qual é a tarefa que deseja atualizar? ")
    if task in tasks:
        index = tasks.index(task)
        new_task = input("Qual é a nova tarefa? ")
        tasks[index] = new_task
        print("Tarefa atualizada com sucesso!")
    else:
        print("Tarefa não encontrada na lista.")

def show_tasks():
    print("Lista de Tarefas:")
    for task in tasks:
        print("- " + task)

while True:
    print("\nSelecione uma opção:")
    print("1. Adicionar Tarefa")
    print("2. Excluir Tarefa")
    print("3. Atualizar Tarefa")
    print("4. Mostrar Tarefas")
    print("0. Sair")
    option = input("> ")

    if option == "1":
        add_task()
    elif option == "2":
        delete_task()
    elif option == "3":
        update_task()
    elif option == "4":
        show_tasks()
    elif option == "0":
        break
    else:
        print("Opção inválida.")