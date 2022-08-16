valores = list()
maior = 0
menor = 0
posmenor = 0

for c in range (0,5):
    valores.append(int(input(f"Insira um valor ({c+1}): ")))

for i in valores:
    if i > maior:
        maior = i
        posmaior = valores.index(i)
        if valores.index(i) == 0:
            menor = i
    
    if i < menor:
        menor = i
        posmenor = valores.index(i)


print(f"O maior número digitado foi {maior} na posição {posmaior+1} e o menor numero digitado foi {menor} na posição {posmenor+1}")

print(valores)