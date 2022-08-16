#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

print('====== EXERCÍCIO 32 ======')
print('')

from calendar import isleap

ano = int(input('Digite um ano: '))
print('')

if isleap(ano):
    print('O ano de {} é bissexto'.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))