#Faça um programa que calcule a soma entre todos números ímpares que são múltiplos de três 
#e que se encontram no intervalo de 1 até 500

print("====== EXERCÍCIO 48 - Soma de ímpares múltiplos de 3 ======")
print("")

s = 0
cont = 0

for c in range(1, 501, 2):
    if c%3 == 0:
        s += c
        cont +=1
print("A soma de todos os {} valores ímpares múltiplos de 3 entre 1 e 500 é {}".format(cont, s))
