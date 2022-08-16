#pessoas = {"nome": "Thomas", "sexo": "M", "idade": 22}
#print(pessoas)
#print(f"O(a) {pessoas['nome']} tem {pessoas['idade']} anos")

#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())

#del pessoas ["sexo"]

#pessoas["nome"] = "Alberto"

#for k, v in pessoas.items():
#    print(k, v)

#brasil = list()
#estado1 = {"uf": "Rio de Janeiro", "sigla": "RJ"}
#estado2 = {"uf": "São Paulo", "sigla": "SP"}

#brasil.append(estado1)
#brasil.append(estado2)

#print(brasil[0]["uf"], brasil[0]["sigla"], )

estado = dict()
brasil = list()

for c in range (0, 3):
    estado["uf"] = input("Unidade Federativa: ")
    estado["sigla"] = input("Sigla do estado: ")
    brasil.append(estado.copy()) #MUITO IMPORTANTE: Esse copy faz com que ele cria uma copia daquele dicionário, sem o copy os dados da lista anterior seriam perdidos.
    
for e in brasil: #Para cada (e)lemento em brasil 
    for v in e.value(): #Para cada valor de e #e = 0 ----> brasil[0][valores]
        print(v) #Exiba valor


