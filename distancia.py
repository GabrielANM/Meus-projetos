x1 = int(input("digite a primeira cordenada: "))
y1 = int(input("digite a primeira cordenada: "))
print()
x2 = int(input("digite a segunda cordenada: "))
y2 = int(input("digite a segunda cordenada: "))
print()

if x1 - x2 >= 10 or x1 - x2 <= -10 or y1 - y2 >= 10 or y1 - y2 <= -10:
    print("longe")
else:
    print("perto")    
