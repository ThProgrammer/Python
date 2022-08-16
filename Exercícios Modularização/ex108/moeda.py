def format(res, moeda="R$"):
    return (f"{moeda}{res:.2f}".replace(".", ","))

#
def metade(n):
    res = n/2
    return res
#

#
def dobro(n):
    res = n*2
    return res
#

#
def aumentar(n, percent):
    res = n + (n * (percent/100))
    return res
#

#
def diminuir(n, percent):
    res = n - (n * (percent/100))
    return res
#    

#TENTATIVA 1: FUNCIONA MAS COM CTZ TEM ALGUM JEITO MELHOR
"""def format(res):
    n = res
    f = str(n)
    
    if n//1 == n:
        return (f"R${int(n)},{f[len(f)-1]*2}")
    else:
        return (f"R${int(n)},{(n-(n//1))*100:.0f}")"""

#TENTATIVA 2 
"""def format2(res): #Ideia by mesquita
    n = res
    f = str(n) #Convertemos o parâmetro para String
    floats = ","

    dec = f.find(".") #Adaptação: Encontra o índice do "."
    for i in range(dec+1, len(f)):
        floats += f[i] #Anota todos os itens depois do "."
    
    if floats == ",0":
        floats = ",00"

    return (f"R${int(n)}{floats[0:3]}")"""

#TENTATIVA 2.1 (elegida melhor)
"""def format(res): 
    n = res
    f = f"{n:.2f}"
    f = str(f)
    dec = f.find(".")

    return (f"R${int(n)},{f[dec+1:]}")"""