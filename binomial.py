def fatorial (numero):
    n = numero
    fatorial = 1
    passagem = False
    conta = numero * (numero - 1)
    n = n - 1

    if numero < 0:
        return 0
    if numero == 2:
        return conta
    else:
        while not passagem:
            if numero == 0 or numero == 1:
                return 1
                passagem = True
            else:
                n = n - 1
                if n > 0:
                    fatorial = conta * n
                    conta = fatorial
                else:
                    passagem = True
                    return fatorial

def binomial (n, k):
    if (n - k) < 0:
        return 0
    print(fatorial(n) / (fatorial(k) * fatorial( n - k)))