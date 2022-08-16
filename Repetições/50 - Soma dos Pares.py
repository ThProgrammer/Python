#Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-o.

s = 0
count = 0

for i in range(1, 7):
    n = int(input("Digite um número inteiro: "))
    if n%2 == 0:
            s = s+n
            count+=1

print("A soma dos {} valores ímpares solicitados é igual a {}".format(count, s))