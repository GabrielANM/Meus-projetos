numero = int(input("Digite o valor de n: "))

passagem = False
impar = 1
x = 1
print(1)

while not passagem:
    if x < numero:
        impar = impar + 2
        print(impar)
        x = x + 1
    else:
        passagem = True