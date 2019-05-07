x = int(input("Digite o valor da largura: "))
y = int(input("Digite o valor da altura: "))

largura = 1
altura = 1

while altura <= y:
    if altura > 1 and altura < y:
        while largura <= x:
            if largura == 1 or largura == x:
                print("#", end = "")
            else:
                print(" ", end = "")
            largura = largura + 1
    else:
        while altura <= y:
            while largura <= x:
                print("#", end = "")
                largura = largura + 1
            break
    altura = altura + 1
    largura = 1
    print()