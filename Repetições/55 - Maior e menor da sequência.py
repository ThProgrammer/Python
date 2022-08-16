# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. 
# No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for i in range (1, 6):
    p = float(input("Digite o peso da {} pessoa: ".format(i)))
    if i == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print("O menor peso é {} Kg e o maior peso é {} Kg.".format(menor, maior))