count18 = 0
counth = 0
countm20 = 0


while True:
    
    i = int(input("Idade: "))

    g = " "
    while g not in "MF":
        g = str(input("Gênero [M/F]: "))[0].upper().strip()

    #Análise dos Dados
    if i >= 18:
        count18 += 1
    
    if g in "Mm":
        counth += 1
    
    if g in "Ff" and i >= 20:
        countm20 += 1

    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Deseja continuar? [S/N]: "))[0].upper().strip()
    if continuar in "N":
        break

print(f"""
====== Fim do programa. ======

Foram cadastradas:

{count18} pessoas maiores de 18 anos.
{counth} homens.
{countm20} mulheres maiores de 20 anos.
""")