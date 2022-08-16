#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa
#O salário do comprador e em quantos anos ele vai pagar
#Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print('====== EXERCÍCIO 36 ======')
print('Olá, seja bem vindo ao nosso programa, nos forneça algumas informações e calcularemos a viabilidade do seu empréstimo')

vc = float(input('Qual o valor da casa? '))
sc = float(input('Qual o seu salário? '))
a = float(input('Em quantos anos você pretende pagar? '))
p = vc / (a*12)

if p <= sc*0.30:
    print('Parabéns, seu empréstimo foi aprovado!')

else:  
    print('Sinto muito, não será possível realizar seu empréstimo.')

