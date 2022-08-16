#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e 0,45 para viagens mais longas.

d = float(input('Qual a distância da sua viagem em km? '))

if d<201:
    p = d*0.50
else:
    p = d*0.45

print('O preço da sua viagem é de R${}'.format(p))