#Exercício Python 52: Faça um programa que leia um número inteiro 
#e diga se ele é ou não um número primo.

print("====== 52 - Números Primos ======")
print("")

n = int(input("Digite um número: "))
d = 0

for p in range(1 , n+1):
    if n%p == 0:
        d +=1

if d == 2:
    print('O numero {} foi divisível {} vezes. Por isso é primo'.format(n, d))
else:
    print("O número {} foi divisivel {} vezes. Por isso não é primo".format(n, d))