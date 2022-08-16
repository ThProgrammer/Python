from random import randrange

npc = 0
nj = 0
s = 0
countv = 0

while True:

    #Escolhendo os números e par ou impar
    npc = randrange(0,6)
    nj = int(input("Escolha seu número: "))
    parouimpar = str(input("Par ou Ímpar?: "))[0].upper().strip()
    s = nj + npc

    #Categorizando o resultado em par ou impar
    if s%2 == 0:
        pi = "P"
        print(f"""
Você escolheu {nj} e eu escolhi {npc}! {nj} + {npc} = {s}, é PAR""")

    else: 
        pi = "I"
        print(f"""
Você escolheu {nj} e eu escolhi {npc}! {nj} + {npc} = {s}, é ÍMPAR""")

    #Declarando o ganhador
    if pi == parouimpar:
        print("""Você venceu!
Vamos jogar novamente!
""")
        countv += 1

    else:
        print("Você perdeu!")
        break

print(f"""
Game Over! Você venceu {countv} vezes consecutivas!""")