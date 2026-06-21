'''Crie um programa que peça para o usuário inserir um login e uma senha. Caso os valores sejam iguais, informar que os
dados são inválidos e pedir novamente as informações. Caso contrário, exibir a mensagem "Bem-vindo ao sistema!".'''

while(True):

    login = input("Digite seu login:")
    senha = input("Digite sua senha:")

    if login == senha:
        print("Os dados estão inválidos, por favor insira novamente")
    else:
        print("Bem vindo ao sistema")
        break




