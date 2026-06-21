while(True):

    productName = input("Insira o nome do produto: ")
    productValue = float(input("Insira o valor do produto: "))
    productQuantity = int(input("Insira a quantidade de produtos que você vai comprar: "))
    total = productValue * productQuantity

    if productName == "" or productValue == 0 or productQuantity == 0 :
        print("Os valores não podem ser vazios, por favor digite novamente")

    else:
        if productName and productQuantity and productValue != 0:
            carrinho = input("Você deseja inserir mais produtos? Digite 1 para sim ou 2 para não")

            if carrinho == 1 :
                productName = input("Insira o nome do produto: ")
                productValue = float(input("Insira o valor do produto: "))
                productQuantity = int(input("Insira a quantidade de produtos que você vai comprar: "))

                

            else:
                print("O valor total da compra de:", productName,"x", productQuantity, "é de:", total)
                break





