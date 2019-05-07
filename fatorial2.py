def fatorial(n):
    x = 1
    if n >= 0: 
        conta = x
        y = n
        while x < y:
            conta = x * n
            n = conta
            x = x + 1
        print(conta)


x = 1
while x >= 0:
    x = int(input("Digite o valor que deseja calcular o fatorial: "))
    fatorial(x)
