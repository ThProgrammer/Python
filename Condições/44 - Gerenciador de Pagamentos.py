
#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto

#– à vista no cartão: 5% de desconto

#– em até 2x no cartão: preço formal 

#– 3x ou mais no cartão: 20% de juros

print("====== EXERCÍCIO 44 - Gerenciador de Pagamentos ======")
print('')

pn = float(input("Preço das compras: R$"))

print("FORMAS DE PAGAMENTO:")
print("[ 1 ] à vista dinheiro/cheque.")
print("[ 2 ] à vista no cartão.")
print("[ 3 ] em até 2x no cartão.")
print("[ 4 ] 3x ou mais no cartão.")

print("")

f = int(input("Qual a forma de pagamento? "))

print("")

if f == 1:
    pa = pn - (pn*0.1)
    print("Parabéns! Você consegui um desconto de 10%.")

elif f == 2:
    pa = pn - (pn*0.05)
    print("Parabéns! Você conseguiu um desconto de 5%.")

elif f == 3:
    pa = pn
    
elif f == 4:
    pa = pn + (pn*0.2)
    x = int(input('Em quantas parcelas será feita o pagamento? '))
    print("Sua compra será parcelada em 10x no valor de {} com juros simples de {} reais.".format(pn/x, pn*0.2/10))
    
else:
    print("ERRO: Forma de pagamento não reconhecida, por favor insira uma forma de pagamento válida.")



# ====== SOBRE O PRINT FINAL ======

if f == 3:
    print("A sua compra vai custar R${}.".format(pn))
    
else:
    print("A sua compra de {} vai custar R${}".format(pn,pa))

print("")