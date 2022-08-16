t = int(input("Quantos termos você quer mostrar? "))
countt = 2

t1 = 0
t2 = 1

print(t1, t2, end=" ")

while countt != t:
    t3 = t1 + t2
    print(t3, end=" ")
    t1 = t2
    t2 = t3
    countt += 1

