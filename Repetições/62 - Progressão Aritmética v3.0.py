a1 = int(input("Primeiro Termo: "))
r = int(input("Razão: "))
t = 0
p = 1

print(a1)

while t != 9: #Mostrar 10 termos da PA
    a1 += r
    t += 1
    print(a1)

if t == 9:
    while p != 0:
        mt = 0
        p = int(input("Devo te mostrar mais quantos termos? ")) #Mostrar mais termos da PA
        while mt != p:
            p = p
            mt += 1
            a1 += r
            print(a1)
    
print("Ok, até a próxima!")

