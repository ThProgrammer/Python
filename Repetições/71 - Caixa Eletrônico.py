count50 = 0
count20 = 0
count10 = 0
count1 = 0

valor = int(input("Qual o valor que você quer sacar? "))

while valor >= 50:
    valor -= 50 #Torre de Hanoi com valor = valor-50
    count50 += 1

while valor >= 20:
    valor -= 20
    count20 += 1

while valor >= 10:
    valor -= 20
    count10 += 1

while valor >= 1:
    valor -= 1
    count1 += 1

#Saída de dados.

print ("""
O valor requisitado será distribuido em:""")

if count50 > 0:
    print(f"{count50} cédulas de 50")

if count20 > 0:
    print(f"{count20} cédulas de 20")

if count10 > 0:
    print(f"{count10} cédulas de 10")

if count1 > 0:
    print(f"{count1} cédulas de 1")

