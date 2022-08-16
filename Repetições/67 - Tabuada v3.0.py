n = 0

while True:
    n = int(input("Quer ver a tabuada de qual valor? (Negativo para parar): "))
    if n < 0:
        break
    print("")
    for t in range (1,11,1):
        print(f"{n}x{t} = {n*t}")

print("Programa encerrado. Volte sempre!")
    