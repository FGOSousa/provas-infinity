
alunos=[]

while True:

    print('-----------------------------------------------')
    print('1 - Adicionar aluno')
    print('2 - Remover aluno')
    print('3 - Visualizar alunos')
    print('4 - Sair do programa')
    print('-----------------------------------------------')

    opcao=input('Escolha uma das opções acima: ')

    if opcao=="1":
        nome=input('Digite nome do aluno: ')
        matricula=input('Adicione número da matricula: ')
        novo_aluno= {
            "nome": nome, 
            "matricula": matricula
        }

        alunos.append(novo_aluno)
    elif opcao == "2":
        matricula=input("Digite o número da matricula do aluno a ser removido: ")

        for i in range(len(alunos)):
            if alunos[i]["matricula"] == matricula:
                del alunos[i]

    elif opcao == "3":
        for i in range(len(alunos)):
            print(f'Aluno: ', (alunos[i]['nome']))
            print(f'Matricula: ', (alunos[i]['matricula']))
            print('--------------------------\n')
    elif opcao == "4":
        break

