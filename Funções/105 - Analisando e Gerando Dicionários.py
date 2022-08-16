def notas(*n, sit = False):
#FALTA O DOCSTRING!!!!!!!!
    booknote = dict()
    booknote["Quantidade de notas"] = len(n)
    booknote["Maior nota"] = max(n)
    booknote["Menor nota"] = min(n)
    booknote["Média"] = sum(n)/len(n)

    if sit:    
        if booknote["Média"] >= 6: booknote["Situação"] = "Boa"
        else: booknote["Situação"] = "Ruim"

    return booknote

#PROGRAMA PRINCIPAL
print(notas(6, 6, 8, 9, 4, sit=True))