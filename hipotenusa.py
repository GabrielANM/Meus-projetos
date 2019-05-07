import math 

def e_hipotenusa(n):
    cateto_oposto = 1
    cateto_adjacente = 1
    hipotenusa = 0
    conta = 1
    ultimo_numero = 1
    while cateto_oposto <= n:
        while cateto_adjacente <= n:
            hipotenusa = math.sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2)
            if hipotenusa % 1 == 0 and hipotenusa <= n:
                conta = hipotenusa
                break           
            cateto_adjacente = cateto_adjacente + 1
        if conta > ultimo_numero:
            print(conta,",",end=" ")
        ultimo_numero = conta



        cateto_oposto = cateto_oposto + 1
        cateto_adjacente = 1
        
            

