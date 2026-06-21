'''Crie um programa que gere a série de Fibonacci enquanto o valor for menor que um valor informado pelo usuário. Observação:
 série de Fibonacci = 0, 1, 1, 2, 3, 5, 8 ,13, 21, 34, 55, ... é formada por 0, 1 e, partir deste ponto, sempre será a soma dos dois valores anteriores.'''

serie1 = 0
serie2 = 1

num = int(input(("Digite um número inteiro, vamos gerar a série de Fibonacci até que cheguemos no valor inserido.")))

print("Sequência de Fibonacci até o número:", num)
print(serie1)
print(serie2)

while (True):

    proximo = serie1 + serie2
    if proximo > num:
        break

    print(proximo)
    serie1 = serie2
    serie2 = proximo









