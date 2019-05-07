numero = int(input("Digite um numero inteiro: "))

passagem = False
digito = 0

while not passagem:
    if numero != 0:
        digitoVariavel = numero % 10
        digito = digito + digitoVariavel
        numero = numero // 10
    else:
        passagem = True
        print(digito)