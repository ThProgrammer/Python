#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR

print('====== EXERCÍCIO 30 ======')
print('')

n = int(input("Digite um número: "))
dn = n%2

print('')

if dn == 0:
    print('O número {} é par!'.format(n))

else:
    print('O número {} é ímpar!'.format(n))
