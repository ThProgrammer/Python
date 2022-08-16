#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais.

n1 = float(input("Digite um valor: "))
n2 = float(input("Digite outro valor: "))

if n1 > n2:
    print('O primeiro valor ({}) é maior'.format(n1))
elif n1 < n2:
    print('O segundo valor ({}) é maior'.format(n2))
else:
    print('Não existe valor maior, pois os dois são iguais.')