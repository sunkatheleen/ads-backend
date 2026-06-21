#Nome: Katheleen Meneses Santiago
#Curso: Análise e Desenvolvimento de Sistemas PUC-PR, campus Londrina

menuPrincipal: str = "Menu principal: 1. Estudantes, 2. Disciplinas, 3. Professores, 4. Turmas, 5. Matrículas, 6. Sair"
menuDeOperacoes: str  = "Menu de operações: 1. Incluir 2. Listar 3. Atualizar 4. Exluir 5. Voltar ao menu principal"

estudantes = []

print("Olá! Seja bem vindo ao sistema de gestão de dados")

while True:

    print(menuPrincipal)

    try:
        inputUser = int(input("Escolha qual opção deseja acessar:"))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        continue

    if inputUser == 1:
        print("A opção escolhida foi: Opção 1. Estudantes")

        while True:
            print(menuDeOperacoes)

            try:
                inputOperacao = int(input("Escolha qual opção deseja acessar (número): "))
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")
                continue

            if inputOperacao == 1:
                print("Você escolheu a opção 1. Incluir")
                nomeEstudante = input("Digite o nome do estudante: ")
                estudantes.append(nomeEstudante)
                print(f"Estudante {nomeEstudante} incluído com sucesso!")

            elif inputOperacao == 2:
                print("Você escolheu a opção 2. Listar")
                if len(estudantes) == 0:
                    print("Não há estudantes cadastrados.")
                else:
                    print("Lista de estudantes:")
                    for estudante in estudantes:
                        print(estudante)

            elif inputOperacao == 3:
                print("Opção 3: Atualizar - EM DESENVOLVIMENTO")

            elif inputOperacao == 4:
                print("Opção 4: Excluir - EM DESENVOLVIMENTO")

            elif inputOperacao == 5:
                break

            else:
                print("Opção inválida, escolha novamente.")

    elif inputUser in [2, 3, 4, 5]:
        print(f"A opção escolhida foi: Opção {inputUser} - EM DESENVOLVIMENTO")

    elif inputUser == 6:
        print("Saindo do sistema.")
        break

    else:
        print("Opção inválida, escolha novamente.")

print("Fim da aplicação.")







