numeros = []
resp = "S"
count = 1 

while resp in "Ss":
    n = (int(input(f"Insira um valor ({count}): ")))
    if n not in numeros:
        numeros.append(n)
        print("Valor adicionado, quer continuar? [S/N]", end=" ")
        
    else:
        del(n)
        print(f"Valor duplicado, não vou adicionar, quer continuar? [S/N]", end=" ")
    
    resp = str(input())
    count +=1

print(sorted(numeros))