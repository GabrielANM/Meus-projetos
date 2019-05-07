def usuario_escolhe_jogada(n, m):
    x = int(input("\nQuantas peças você vai tirar? "))
    passagem = False
    while not passagem: 
        if x < 1 or x > m:
            print("\nOops! Jogada inválida! Tente de novo.")
            x = int(input("\nQuantas peças você vai tirar? "))
        else:
            print(x)
            break
n = int(input("Quantas peças? "))
m = int(input("Limite de peças por jogada? "))

usuario_escolhe_jogada(n, m)