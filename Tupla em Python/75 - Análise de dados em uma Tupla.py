ns = (int(input("Digite um número: ")),
int(input("Digite outro número: ")),
int(input("Digite mais um número: ")),
int(input("Digite o último número: ")),)

print(ns)

print(f"O número nove apareceu {ns.count(9)} vezes")

if 3 in ns:
        print(f"O primeiro '3' foi digitado na {ns.index(3)+1}° posição")
else:
    print(f"O número 3 não foi digitado")

print("Os números pares digitados foram: ")
for i in ns:
    if i %2 == 0:
        print(i, end=" ")
