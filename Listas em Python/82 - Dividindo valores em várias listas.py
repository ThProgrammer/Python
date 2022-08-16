valores = []
impar = []
par = []
resp = "S"
count = 1

while resp in "Ss":
    valores.append(int(input(f"Insira um valor ({count}): ")))
    resp = str(input("Deseja continuar? [S/N]: "))
    count+=1

for numero in valores:
    if numero %2 == 0:
        par.append(numero)

    else:
        impar.append(numero)


print(f"""Lista com todos os valores: {valores})
Lista de valores pares: {par}
Lista de valores impares: {impar}""")