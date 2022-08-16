soma = 0
count1000 = 0
nomebarato = " "
maisbarato = 0
pvez = 0

while True:

    produto = input("Produto: ")
    preço = (input("Preço: "))
    
    if preço > 1000:
        count1000 += 1

    if pvez == 0:
        maisbarato = preço
        nomebarato = produto
        pvez += 1
        
    else:
        if preço < maisbarato:
            maisbarato = preço
            nomebarato = produto

    soma += preço

    resp = " "
    while resp not in "SN":
        resp = input("Deseja continuar? [S/N]: ")[0].upper().strip()
    
    if resp == "N":
        break

print(f"""
====== Fim do programa ======

Foram gastos R${soma}. 
Foram comprados {count1000} produtos acima de R$1000.
O produto mais barato foi {nomebarato}.""")
    