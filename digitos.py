x = int(input("Digite um numero cujos digitos serão somados: "))
print()

soma = 0

while x != 0:
    digito = x % 10
    soma = soma + digito
    x = x // 10

print("A soma dos digitos do numero digitado é:", soma)