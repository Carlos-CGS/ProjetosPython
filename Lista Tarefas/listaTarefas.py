tarefas = []

def add_tarefa():
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print(f'Tarefa "{tarefa}" adicionada!')

def list_tarefa():
    if not tarefas:
        print("Nenhuma tarefa.")
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. {tarefa}")

def remove_tarefa():
    list_tarefa()
    num = int(input("Número da tarefa para remover: "))
    if 0 < num <= len(tarefas):
        removed = tarefas.pop(num - 1)
        print(f'Tarefa "{removed}" removida!')
    else:
        print(f"Erro. Tarefa não localizada.")

while True:
    print("\n1. Adicionar Tarefa\n2. Listar Tarefas\n3. Remover Tarefa\n4. Sair")
    choice = input("Escolha uma das opções acima: ")
    if choice == '1':
        add_tarefa()
    elif choice == '2':
        list_tarefa()
    elif choice == '3':
        remove_tarefa()
    elif choice == '4':
        break
    else:
        print("Opção inválida.")
