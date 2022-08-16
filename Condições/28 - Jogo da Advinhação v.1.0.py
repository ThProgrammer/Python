#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 a 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randrange
from time import sleep

print('====== JOGO DA ADIVINHAÇÃO v.1.0 ======')
print('')


n = randrange(5)


print('Vou pensar em um número de 0 a 5! Tente adivinhar...')
print('')
print('PENSANDO (...)')
sleep(3)
print('')
c = int(input("Em que número pensei? "))

print('')
print('PROCESSANDO...') 
sleep(3)

if c == n:
    print('Você acertou, parabéns! Meu número era o {}'.format(n))
else:
    print('Meu número era o {}, mais sorte da próxima vez :('.format(n))