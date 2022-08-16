from datetime import datetime

trabalhador = dict()

trabalhador["Nome"] = input("Qual seu nome? ")
trabalhador["Idade"] = datetime.now().year - int(input("Qual seu ano de nascimento? "))
trabalhador["Carteira de trabalho"] = int(input("Qual sua carteira de trabalho? [Digite 0 se não tiver]: "))

if trabalhador["Carteira de trabalho"] != 0:
    trabalhador["Ano de contratação"] = int(input("Qual seu ano de contratação? "))
    trabalhador["Salário"] = int(input("Qual seu salário? "))

    if 2022 - trabalhador["Ano de contratação"] >= 0:
        trabalhador["Idade de aposentadoria"] = trabalhador["Idade"] + 35 - (datetime.now().year - trabalhador["Ano de contratação"])

for k, v in trabalhador.items():
    print(f"{k} = {v}")