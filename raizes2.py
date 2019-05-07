import math
def delta(a, b, c):
    return (b ** 2 - 4 * a * c)
def umaRaiz(a, b, x):
    return ((-b + x) / (2 * a))
def duasRaizes(a, b, x):
    return ((-b + x) / (2 * a)), ((-b - x) / (2 * a))   
def raiz(x):
    return math.sqrt(x)
def bhaskara(a, b, c): 
    x = delta(a, b, c)
    if x < 0:
        print("esta equação não possui raízes reais")
    else:
        x = raiz(x)
        if x == 0:
            print(umaRaiz(a, b, x))
        else:
            print(duasRaizes(a, b, x))