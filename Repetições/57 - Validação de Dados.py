
g = str(input("Informe seu gênero [M/F]: ")).strip().upper()[0]

while g not in "MmFf":
    g = str(input("""Resposta inválida, por favor informe seu gênero utilizando "M" ou "F": """)).strip().upper()[0]

print("Gênero {} registrado com sucesso".format(g))