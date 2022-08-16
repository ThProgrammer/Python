aluno = dict()

aluno["Nome"] = input("Nome do aluno: ")
aluno["Média"] = int(input(f"Média de {aluno['Nome']}: "))

if aluno["Média"] <= 5.9:
    aluno["Situação"] = "reprovado"

else:
    aluno ["Situação"] = "aprovado"

for k, v in aluno.items():
    print(f"{k} é igual a {v}")