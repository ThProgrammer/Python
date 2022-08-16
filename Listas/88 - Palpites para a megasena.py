from random import randrange
from time import sleep
numeros = []
listaaux = []

x = int(input("Quantos jogos quer que eu palpite?: "))

for j in range (0,x):
    for i in range(0,6):
        n = randrange(1, 60)
        if n not in numeros:
            numeros.append(n)

    listaaux.append(numeros[:])
    numeros.clear()


#SAÍDA DE DADOS:
for c in range (0, x):    
    print(f"Jogo {c+1}: {listaaux[c]}")
    sleep(2)