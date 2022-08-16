def resumo(n = 0, aumento = 10, redução = 5):
    from titulo import titulo
    res = n
    book = dict()
    book["Preço analisado:"] = output(res)
    book["Dobro do preço:"] = dobro(res, True)
    book["Metade do preço:"] = metade(res, True)
    book[f"{aumento}% de aumento:"] = aumentar (res, aumento, True)
    book[f"{redução}% de redução:\t"] = diminuir (res, redução, True)
    titulo("resumo do valor")
    for k, v in book.items(): print(f"{k} \t{v}")


def metade(n = 0, format = False):
    res = n/2
    if not format: return res 
    else: return output(res)
#

#
def dobro(n = 0, format = False):
    res = n*2
    if not format: return res 
    else: return output(res)
#

#
def aumentar(n = 0, percent = 0, format = False):
    res = n + (n * (percent/100))
    if not format: return res 
    else: return output(res)
    
#

#
def diminuir(n = 0, percent = 0, format = False):
    res = n - (n * (percent/100))
    if not format: return res 
    else: return output(res)
    
#    
def output(res, moeda="R$"):
    return (f"{moeda}{res:.2f}".replace(".", ","))