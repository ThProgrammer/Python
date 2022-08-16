#DECLARAÇÃO DE VARIÁVEIS NECESSÁRIAS:
pessoa = []
pessoaaux = []
pesados = []
leves = []
maiorpeso = 0
menorpeso = 0
c = 1
resp = "S"


#ENTRADA DE DADOS:
while resp in "Ss":
    pessoa.append(str(input("Nome: ")))
    pessoa.append(int(input("Peso: ")))
    
#PROCESSAMENTO:    

    if pessoa[1] > maiorpeso:
        maiorpeso = pessoa[1]
        if c == 1:
            menorpeso = pessoa[1]
    
    if pessoa[1] < menorpeso:
        menorpeso = pessoa[1]

    pessoaaux.append(pessoa[:])
    resp = str(input("Deseja continuar? [S/N]: "))
    c+=1
    pessoa.clear()


for p in pessoaaux:
    if p [1] == maiorpeso:
        pesados.append(p)
    
    if p [1] == menorpeso:
        leves.append(p)


#SAÍDA DE DADOS:

print(f"Foram cadastradas {len(pessoaaux)} pessoas.")

print(f"As pessoas com o peso mais pesado ({maiorpeso}kg's) foram: ")
for p in pesados:
    print(p[0])

print(f"As pessoas com o peso mais leve ({menorpeso}kg's) foram: ")
for p in leves:
    print(p[0])

    

