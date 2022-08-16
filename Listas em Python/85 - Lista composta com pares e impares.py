numeros = [[], []]

for c in range (0, 7):
    n = int(input(f"Insira o {c+1}° valor: "))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)

print(f"Os valores pares digitados foram: {numeros[0]}")
print(f"Os valores ímpares digitados foram: {numeros[1]}")