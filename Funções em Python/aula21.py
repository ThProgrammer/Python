def teste(b):
    global n #global não funciona da maneira que o guanabara falou, não sei porquê
    n = 8
    b += 1
    print(f"Na função teste, n vale {n}")
    print(f"B vale {b}")


#Programa Principal
n = 2
print(f"No programa principal, n vale {n}")
teste(n)
