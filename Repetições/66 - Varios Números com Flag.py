n = 0
s = 0
countq = 0

while True:
    n = int(input("Digite um valor (999 para parar): "))
    if n == 999:
        break    
    s += n
    countq +=1

print(f"""
A soma dos {countq} valores digitados resulta em {s}""")