#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$12].250,00 calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%

s = float(input('Digite o seu salário: '))


if s > 1250:
    a = s*0.10

else: 
    a = s*0.15

ns = s+a

print('')
print('Seu aumento é de R${} e seu novo salário é de R${}'.format(a,ns))