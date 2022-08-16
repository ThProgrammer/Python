valores = []

resp = "S"
count = 0
while resp in "Ss":
    valores.append(int(input(f"Insira um valor({count+1}): ")))

    count+=1
    resp = str(input(f"{valores[count-1]} adicionado, deseja continuar? [S/N]: "))

valores.sort(reverse=True)
print(f"Foram digitados {count} valores.")
print(f"Valores em ordem decrescente: {valores}") 

if 5 in valores:
    print("O valor 5 foi encontrado.")

else:
    print("O valor 5 não foi encontrado.")
