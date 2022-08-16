

def sortear(lst):
    from random import randrange
    from time import sleep

    print("Sorteando valores para a lista: ", end="")
    for i in range(0, 5):
        lst.append(randrange(1, 10))
        print(lst[i], end=" ", flush=True)
        sleep(0.5)

def somar(lst):
    print("\nValores pares sorteados: ", end="")
    soma = 0
    for i in range (0, len(lst)):
        if lst[i] % 2 == 0:
            print(f"{lst[i]}", end=" ")
            soma += lst[i]
    print(f"\nO total dos valores pares sorteados para a lista é {soma}")


#PROGRAMA PRINCIPAL
numeros = list()
sortear(numeros)
somar(numeros)