

def computador_escolhe_jogada(n, m):
    x = 0
    while x < m:
        x = x + 1
        y = n - x
        if y % (m + 1) == 0:
            print(x)
            break
    if y % (m + 1) != 0:
        print(m)

n = int(input("Quantas peças? "))
m = int(input("Limite de peças por jogada? "))

computador_escolhe_jogada(n, m)
