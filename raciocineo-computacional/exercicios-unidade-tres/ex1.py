'''Laços finitos (for)

Exercício de fixação 1: Crie um programa que solicite ao usuário dez números, contando quantos são pares e quantos são ímpares e informando ao final
 essas informações.'''

numerosPares = 0
numerosImpares = 0

for i in range(10):
    num = int(input("Digite um número:"))
    if num % 2 == 0:
        numerosPares += 1
    else:
        numerosImpares += 1

print("Dos números", numerosPares,"são pares e", numerosImpares, "são impares.")

