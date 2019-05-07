x = int(input("Digite o valor da largura: "))
y = int(input("Digite o valor da altura: "))

largura = 1
altura = 1

while altura <= y:
    while largura <= x:
        print("#", end = "")
        largura = largura + 1
    altura = altura + 1
    largura = 1
    print()