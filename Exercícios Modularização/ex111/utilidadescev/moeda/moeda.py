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
    from ex111.utilidadescev.dado.dado import red
    try: return (f"{moeda}{res:.2f}".replace(".", ","))
    except: print(red("Dados não informados."))


#
def resumo(n = "void", aumento = 10, redução = 10):
    from titulo import titulo

    res = n
    try: float(res)
    except: 
        print("Número não informado!")
        return
    titulo("resumo")
    print(f"Preço a ser analisado: \t{output(res)}")
    print(f"Dobro do preço: \t{dobro(res, True)}")
    print(f"Metade do preço: \t{metade(res, True)}")
    print(f"{aumento}% de aumento: \t{aumentar(res, aumento, True)}")
    print(f"{redução}% de redução: \t{diminuir(res, redução, True)}\n"+"-"*33+"\n")