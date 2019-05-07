laço = int(input("Quantos numeros você deseja somar? "))

print ()
incremento = 1
soma = 0
while incremento <= laço:
     valor = int(input("Digite um valor a ser somado:"))
     soma = soma + valor 
     incremento = incremento + 1
print()
print("O valor total da soma é:", soma)     