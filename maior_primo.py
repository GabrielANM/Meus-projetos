def éPrimo(n):
    passagem = False
    x = 1
    if n == 2:
        return n
    while x < (n - 1) and not passagem:
        x = x + 1
        if n % x == 0:
            return 0
            passagem = True    
        if x == (n - 1):
            return n

def maior_primo(n):
    x = 1
    while x < n:
        x = x + 1
        if éPrimo(x) != 0:
            maiorPrimo = éPrimo(x)
            

    return maiorPrimo
        


    
            

            

