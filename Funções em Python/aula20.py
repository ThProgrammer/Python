#FUNÇÕES:

def Linha():
    print("-"*30)

def Mensagem(msg):
    Linha()
    print(msg)
    Linha()

def Soma (n1, n2):
    return(n1+n2)
#def Soma (n1, n2):
    print(f"n1 = {n1}, n2 = {n2}")
    print(f"n1 + n2 = {n1+n2}")

def Contador (* n): #* n Indica ao python que não saberemos quantos parâmetros receberemos, todos recebidos entrarão na tupla N
    return len(n)

def Dobra (lst):
    for i in range(0, len(lst)):
        lst[i] *= 2
    print(lst)

#def Contador (* n):
    #count = 0
    #for valor in n:
        #count+=1
    #print(count) #Ao tentar print ao invés de "return" dentro do print abaixo, ele buga e diz "None"

#PROGRAMA PRINCIPAL

Mensagem("ESTOU ENTRE LINHAS")

print(f"Foram inseridos {Contador(5, 2, 3)} valores")
print(Soma(n1 = 10, n2 = 4))
#print(Soma(n1 = int(input("n1: ")), n2 = int(input("n2: "))))
#Soma(4, 10)
Dobra([5, 2, 1, 7, 9])




