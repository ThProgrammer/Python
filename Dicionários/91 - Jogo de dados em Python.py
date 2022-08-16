from random import randrange
from time import sleep
from operator import itemgetter #Import para indicar com base no que ordenaremos o dicionário.

#jogadores = {"jogador1": randrange(0, 6), "jogador2": randrange(0, 6), "jogador3": randrange(0, 6), "jogador4": randrange(0,6)}
jogadores = dict()
ranking = list()

for i in range(1, 5):
    jogadores[f"jogador {i}"] = randrange(0,6)


for k, v in jogadores.items():
    print(f"O {k} tirou {v} no dado.")
    sleep(1)

ranking = sorted(jogadores.items(), key = itemgetter(1), reverse = True) 

#É assim que organiza um dicionario. Criando uma lista e usando sorted()
#Utiliza jogadores.items porque organizaremos tanto as keys quanto os values do dicionarios
#E usaremos os VALUES como base para ordenar, logo indicamos isso com o "key = itemgetter(1)" sendo itemgetter(0) as keys, e itemgetter (1) os values
#E usamos reverse = True pra ser em ordem decrescente.

for i, v in enumerate (ranking): #Não usamos ranking.items() pois não é um dicionário, e sim uma lista com tuplas dentro
    print(f"Em {i+1}º lugar: {v[0]} com {v[1]}")