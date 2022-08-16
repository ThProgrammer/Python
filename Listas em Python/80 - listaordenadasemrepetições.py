valores = []
countpos = 0
for c in range (0,5):

    n = int(input(f"Insira um valor ({c+1}): "))

    for i in range (0, len(valores)):
        if n > valores[i]:
            countpos+=1
            
    valores.insert(countpos, n)
    countpos = 0
print(valores)