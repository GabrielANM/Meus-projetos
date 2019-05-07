import math
a = float(input("digite o valor da variavel a:"))
b = float(input("digite o valor da variavel b:"))
c = float(input("digite o valor da variavel c:"))
print()
delta = (b ** 2 - 4 * a * c)
if delta < 0:
    print("esta equação não possui raízes reais")
else:
    delta = math.sqrt(delta)
    if delta == 0:
        r1 = ((-b + delta) / (2 * a))
        print("a raiz desta equação é", r1)
    else:
        r1 = ((-b + delta) / (2 * a))
        r2 = ((-b - delta) / (2 * a))
        if r1 > r2:
            print("as raízes da equação são", r2, "e", r1)  
        else:
            print("as raízes da equação são", r1, "e", r2) 