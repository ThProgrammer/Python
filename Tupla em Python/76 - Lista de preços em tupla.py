#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.


produtos = ("Lápis", 1.75, "Borracha", 2, "Caderno", 15.90)

for i in range (0, len(produtos)):
    if i%2 == 0:
        print(f"{produtos[i]:.<30}", end= "") #end= "" pra não quebrar de linha
    else:
        print(f"R${produtos[i]}")