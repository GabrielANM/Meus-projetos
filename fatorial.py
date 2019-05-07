numero = int(input("Digite o valor de n: "))
n = numero
fatorial = 1
passagem = False
conta = numero * (numero - 1)
n = n - 1

if numero == 2:
    print(conta)
else:
    while not passagem:
        if numero == 0 or numero == 1:
            print("1")
            passagem = True
        else:
            n = n - 1
            if n > 0:
                fatorial = conta * n
                conta = fatorial
            else:
                passagem = True
                print(fatorial)             