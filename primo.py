numero = int(input("Digite um numero inteiro: "))

passagem = False
divisor = numero
primo = float
if numero == 1:
    print("não primo")

while not passagem and divisor != 1:
    divisor = divisor - 1
    if divisor != 1:
        primo = numero / divisor
        if (primo % 1) == 0:
            print("não primo")
            passagem = True

if divisor == 1 and numero != 1:
    print("primo")
    






    