cadastro = list()


for a in range (0,2):
    nome = str(input("Insira o nome do aluno: "))
    nota1 = int(input("Insira a 1° nota: "))
    nota2 = int(input("Insira a 2° nota: "))
    media = (nota1+nota2)/2
    cadastro.append([nome, [nota1, nota2], media])

#SAÍDA DE DADOS:

for n in range (0,2):
        print(f"(Aluno {n}) ======= {cadastro[n][0]}")
        print(f"Média: ========== {cadastro[n][2]}")


while True:
    n = int(input("Deseja ver as notas de algum aluno? (999 para parar): "))
    if n == 999:
        break
    print(f"""Notas do {cadastro[n][0]} = {cadastro[n][1]}""")