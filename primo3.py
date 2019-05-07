def calcula_primo(x):
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

def n_primos(x):
    cont = 2
    primo = 1
    numeros_primos = 0
    while cont <= x:
        primo = calcula_primo(cont)
        if primo:
            numeros_primos = numeros_primos + 1
        cont = cont + 1
    return numeros_primos
