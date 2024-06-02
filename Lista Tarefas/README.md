# Gerenciador de Tarefas Simples

Este é um aplicativo simples de gerenciador de tarefas escrito em Python. Ele permite adicionar, listar e remover tarefas de uma lista. O aplicativo é interativo e funciona na linha de comando.

### Descrição das Funções
> add_task() - Adiciona uma nova tarefa à lista de tarefas.
- Solicita ao usuário que digite a descrição da tarefa.
- Adiciona a tarefa à lista tasks.
- Imprime uma mensagem de confirmação.

> list_tasks() - Lista todas as tarefas atuais.
- Verifica se a lista de tarefas está vazia.
- Se não estiver vazia, imprime cada tarefa com um número correspondente.

> remove_task() - Remove uma tarefa da lista.
- Lista todas as tarefas atuais.
- Solicita ao usuário que digite o número da tarefa a ser removida.
- Remove a tarefa correspondente da lista.
- Imprime uma mensagem de confirmação.
- Caso o número da tarefa não esteja na lista, apresenta uma mensagem de erro.

> Loop Principal - Executa o aplicativo em um loop contínuo.
- Exibe um menu com opções para adicionar, listar, remover tarefas ou sair.
- Chama a função apropriada com base na escolha do usuário.
- Sai do loop e termina o programa se o usuário escolher a opção de sair.