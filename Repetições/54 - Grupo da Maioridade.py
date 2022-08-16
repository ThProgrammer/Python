#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. 
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year

maiores = 0
menores = 0

for i in range (1, 8):
    anos=int(input("Digite o ano que você nasceu: "))
    if atual - anos >=18:
        maiores += 1
    else:
        menores += 1 

print("{} das 7 pessoas já atingiram a maioridade e {} ainda são menores.".format(maiores, menores))
