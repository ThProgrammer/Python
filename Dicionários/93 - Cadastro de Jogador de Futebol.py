jogador = {}
gol = list()
jogador["nome"] = input("Qual o nome do jogador? ")
jogador["partidas"] = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

for c in range (0, jogador["partidas"]):
    gol.append(int(input(f"     Quantos gols ele fez na {c+1}° partida? ")))
    
jogador["gols"] = gol[:]
jogador["total"] = sum(jogador["gols"])
    

#SAÍDA DE DADOS
print(f"\nO jogador {jogador['nome']} jogou {jogador['partidas']} partidas.")

for c in range (0, jogador["partidas"]):
    print(f"=> Na partida {c+1}, fez {jogador['gols'][c]} gols.")

print(f"Foi um total de {jogador['total']} gols.")