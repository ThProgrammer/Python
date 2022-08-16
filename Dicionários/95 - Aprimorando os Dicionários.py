grupo = list()
jogador = dict()
golaux = list()

#ENTRADA DE DADOS:
while True:
    #CADASTRANDO OS DADOS NO DICIONÁRIO
    jogador["nome"] = input("Nome do jogador: ")
    jogador["partidas"] = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

    for c in range (0, jogador["partidas"]):
        golaux.append(int(input(f"Quantos gols ele fez na {c+1}º partida?")))
    
    jogador["gols"] = golaux[:] #recebe uma copia da lista 

    jogador["total"] = sum(golaux) #sum = soma de todos os elementos da lista.

    grupo.append(jogador.copy()) #recebe uma *copia* de jogador (.copy() é muito importante, pois se não ele interligaria todas as listas jogadores criadas.)

    #LIMPANDO PARA RECEBER OS PROXIMOS DADOS
    golaux.clear() 
    for v in jogador.values(): 
        del v

    resp = input("Deseja continuar? [S/N]: ")[0].strip()
    if resp in "Nn": break

#PAINEL DE ACESSO:
print("=-"*30)
for c in range (0, len(grupo)): #MEXE AQUI PRA DEIXAR BONITO
    print(f"{c} {grupo[c]['nome']}  {grupo[c]['gols']}  {grupo[c]['total']}")


codigo = int(input("Mostrar dados de qual jogador?(break: 999): "))

#SAÍDA DE DADOS:
while codigo != 999:

    print(f"\n-- LEVANTAMENTO DO JOGADOR: {grupo[codigo]['nome']}")
    for c in range(0, grupo[codigo]['partidas']):
        print(f"        No jogo {c} fez {grupo[codigo]['gols'][c]} gols.")

    #VALIDAÇÃO DE DADOS DO CÓDIGO DO JOGADOR:
    while True:
        codigo = int(input("Mostrar dados de qual jogador? (break: 999): "))
        if codigo < 0 or (codigo > len(grupo) and codigo != 999):
            print(f"ERRO! Não existe jogador com código {codigo}, Tente novamente!: ")
        else: break

print("<<< Volte sempre >>>")