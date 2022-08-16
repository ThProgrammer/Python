#Faça um programa que leia um número qualquer e mostre o seu factorial.

f = int(input("Digite um número: "))
n = f
m = f - 1

#m = f-1 (ex: 5 - 4) e f = f*m, esse loop atualizará tanto F quanto M, até M = 0
while m != 0:
    f = f * m
    m -= 1

print("{}! é igual a {}".format(n, f))