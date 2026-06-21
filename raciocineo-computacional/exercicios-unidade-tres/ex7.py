'''Crie um programa que solicite ao usuário vários números e, ao digitar 0, calcule a média
dos números informados.'''

contador = 0
soma = 0

while(True):
    num = int(input("Digite vários números para calcularmos a média entre eles. A média será calculada "
                    "quando você digitar 0. "))

    if num == 0:
        break

    else:
        soma += num
        contador += 1


if contador > 0:
    media = soma / contador
    print("A média entre os números é:", media)

else:
    print("Nenhum número foi informado")


