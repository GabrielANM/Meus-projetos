def primo(x):
    cont = 1
    primo = 0
    while cont >= 1 and cont <= (x / 2):
        cont = cont + 1
        primo = x % cont
        if primo == 0 and x != 2:
            return False
            break
    if primo != 0 or x == 2:
        return True

x = int(input("digite um numero inteiro maior que 1 ou 0 para encerrar o programa: "))

while x != 0:
    print(primo(x))
    x = int(input("\ndigite um numero inteiro maior que 1 ou 0 para encerrar o programa: "))

