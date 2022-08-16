grupo = []
pessoa = {}
soma = 0
resp = "s"

while resp in "Ss":
    pessoa["nome"] = input("Qual seu nome? ")
    pessoa["genero"] = input("Qual seu gênero? (M/F): ")[0].upper()
    pessoa["idade"] = int(input("Qual sua idade? "))
    soma += pessoa["idade"]
    grupo.append(pessoa.copy())
    resp = input("Deseja continuar? [S/N]: ")[0]

media = soma/len(grupo)


#SAÍDA DE DADOS
print(f"\n- O grupo tem {len(grupo)} pessoas.")
print(f"- A média de idade é de {media} anos.")
print("- As mulheres cadastradas foram: ")

for c in range(0, len(grupo)):
    if grupo[c]["genero"] == "F":
        print(grupo[c]["nome"])
    
print("- Lista das pessoas que estão acima da média:")

for c in range(0, len(grupo)):
    if grupo[c]["idade"] > media:
        print(f"Nome = {grupo[c]['nome']}; Gênero = {grupo[c]['genero']}; Idade = {grupo[c]['idade']}")