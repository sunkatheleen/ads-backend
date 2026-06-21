'''Crie um programa que peça dois números ao usuário – o primeiro será o numerador e o segundo, o expoente. A saída do programa
deve ser o resultado da operação: numerador elevado ao expoente. Observação: não use a função própria do Python que calcula
automaticamente potência.'''

numerador = int(input("Digite um número para ser o numerador"));
expoente = int(input("Digite um número para ser o expoente"));
operacao = numerador

for i in range(expoente):

    operacao *= numerador

print(numerador, "elevado a", expoente, "é igual a:", operacao)
