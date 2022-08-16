def metade(n, format = False, moeda = "R$"):
    res = n/2
    if not format: return res 
    else: return output(res)
#

#
def dobro(n, format = False, moeda = "R$"):
    res = n*2
    if not format: return res 
    else: return output(res)
#

#
def aumentar(n, percent, format = False, moeda = "R$"):
    res = n + (n * (percent/100))
    if not format: return res 
    else: return output(res)
    
#

#
def diminuir(n, percent, format = False, moeda = "R$"):
    res = n - (n * (percent/100))
    if not format: return res 
    else: return output(res)
    
#    
def output(res, moeda="R$"):
    return (f"{moeda}{res:.2f}".replace(".", ","))
