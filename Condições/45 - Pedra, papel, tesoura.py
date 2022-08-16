#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randrange
from time import sleep

print("""====== ULTIMATE JOKENPÔ MATCH ======

""")

print("""ACHA QUE É CAPAZ DE VENCER O ULTIMATE JOKENPÔ?: ")

[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA

""")

j = int(input("FAÇA SUA JOGADA: "))
pc = randrange(1, 4)
print("")

if j == 1:
    jogada = "PEDRA"
elif j == 2:
    jogada = "PAPEL"
else:
    jogada = "TESOURA"

if pc == 1:
    resposta = "PEDRA"
elif pc == 2:
    resposta = "PAPEL"
else:
    resposta = "TESOURA"

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!")
sleep(0.5)

print()
print("-="*10)
print("Jogador jogou: {}".format(jogada))
print("ULTIMATE JOKENPÔ jogou: {}".format(resposta))
print("-="*10)
print("")

if j == 1 and pc == 3 or j == 2 and pc == 1 or j == 3 and pc == 2:
    print("JOGADOR VENCE")

elif j == pc:
    print("EMPATE, VAMOS DE NOVO?")

else:
    print("ULTIMATE JOKENPÔ VENCE")


