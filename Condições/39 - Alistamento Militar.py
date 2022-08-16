#Faça um programa que leia o ano de um nascimento de um jovem e informe, de acordo com sua idade:
#- Se ele ainda vai se alistar ao serviço militar.
#- Se é a hora de se alistar
#- Se já passou do tempo do alistamento 
#- Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

print('====== EXERCÍCIO 39 v.2022. ======')

a = int(input('Digite o ano que você nasceu: '))
data = 2022
i = data - a
f = 18 - i
fa = 2022 + f
p = i - 18
pa = 2022 - p

print('Quem nasceu em {} tem {} anos em 2022'.format(a, i))

if data - a == 18:
    print('Chegou a hora de se alistar! ')

elif data - a > 18:
    print('Você já deveria ter se alistado há {} anos'.format(p))
    print('Seu alistamento foi em {}'.format(pa))

else:
    print('Ainda há tempo, seu alistamento será daqui {} anos em {}'.format(f,fa))
