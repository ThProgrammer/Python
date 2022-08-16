n = int(input("Digite um valor: "))

r = "S"
s = n
maior = n
menor = n
ncount = 1

while r in "Ss":
    n1 = int(input("Digite outro valor: "))
    s += n1

    if n1 > maior: #Atribuindo o maior n1 a varíavel
        maior = n1 
    if n1 < menor: #Atribuindo o menor n1 a varíavel
        menor = n1 

    ncount += 1

    r = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]

print("A média dos {} valores digitados foi {}, o maior valor foi {} e o menor valor foi {}.".format(ncount, s/ncount, maior, menor))
