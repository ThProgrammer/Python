def cartola (name = "<unknown>", goals = 0):
    if name in " " or name in "":
        name = "<unknown>"

    ficha = f"O jogador {name} marcou {goals} gol"
    
    #CORREÇÃO DE PLURAL
    if goals > 1 or goals == 0: ficha+="s."
    else: ficha+= "."

    return ficha

#PROGRAMA PRINCIPAL
jogador = input("Insira o nome do jogador: ")
gols = str(input("Insira quantos gols ele marcou: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

print(cartola(jogador, gols))