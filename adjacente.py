numero = int(input("digite um numero: "))

digitoIgual = False

while not digitoIgual:
    ultimoDigito = numero % 10
    digitoSeguinte = (numero % 100) // 10
    if ultimoDigito == digitoSeguinte or numero < 10:
        digitoIgual = True
    else:
         numero = numero // 10


if numero > 10:
    print("sim")
else:
    print("não")


