''' Crie um programa que solicite um número ao usuário e exiba a tabuada dele de 1 a 10, no formato:

Tabuada do n

n x 1 = n

n x 2 = 2n

...

n x 10 = 10n'''

num = int(input("Digite um número para ver a tabuada correspondente:"))

print("Tabuada do", num, ":")

for i in range(1, 11):
    multiplicacao = num * i
    print(num, "x", i, "=", multiplicacao)

