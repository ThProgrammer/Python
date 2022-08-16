def votação (ano):
    from datetime import datetime
    idade = datetime.now().year - ano
    voto = f"Com {idade} anos o status do seu voto é " 
    if idade >= 70 or idade == 16 or idade == 17: voto += "OPCIONAL."
    elif idade >= 18 and idade < 70: voto += "OBRIGATÓRIO."
    else: voto += "NEGADO."
    return voto

#PROGRAMA PRINCIPAL
ano = int(input("Insira seu ano de nascimento: "))
print(votação(ano))