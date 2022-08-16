# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
homens = 0
somaidade = 0
mulhermenorque20 = 0
maioridadehomem = 0

for d in range (1,5):
    print("------ {}° PESSOA ------".format(d))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    genero = str(input("Gênero [M/F]: ")).strip()

    somaidade += idade

    #ATRIBUINDO A MAIOR IDADE DO HOMEM A VARIÁVEL:

    if idade > maioridadehomem and genero in "Mm":
        maioridadehomem = idade
        hmv = nome
        homens =+ 1
    
    #CONTANDO QUANTAS MULHERES TEM MENOS DE 20 ANOS

    if idade < 20 and genero in "Ff":
        mulhermenorque20 += 1

#CUIDANDO DO RESULTADO FINAL

if homens == 0:
    print("""
A média de idade é {} anos.
Não há homens.
Há {} mulheres com menos de 20 anos.""".format(somaidade/4, mulhermenorque20))
        
else:
    print("""
A média de idade é {} anos.
O homem mais velho se chama {}.
Há {} mulheres com menos de 20 anos.""".format(somaidade/4, hmv, mulhermenorque20))