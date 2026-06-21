'''Crie um programa que receba um texto digitado pelo usuário e o imprima apenas com consoantes, removendo as vogais. Observação: desconsiderar
 letras maiúsculas e acentos'''

texto = input("Escreva uma frase para removermos as vogais:")
consoantes = ""

for i in texto:
    if i.lower() not in "aeiou":
        consoantes = consoantes + i

print(consoantes)