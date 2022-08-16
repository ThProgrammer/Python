#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

#if n1 > n2 and n1 > n3:
ma = n1

if n2 > n1 and n2 > n3:
    ma = n2

if n3 > n1 and n3 > n2:
    ma = n3

#if n1 < n2 and n1 < n3
me = n1

if n2 < n1 and n2 < n3:
    me = n2

if n3 < n1 and n3 < n2:
    me = n3

print('')
print('O maior número dentre esses é {} e o menor é {}'.format(ma,me))








#n = input("Digite 3 números: ")
#nl = n.split()

#if nl[0] > (nl[1], nl[2]) :
    #ma = nl[0]

#if nl[1] > (nl[0], nl [2]):
    #ma = nl[1] 

#if nl[2] > (nl[0], nl[1]):
    #ma = nl [2]

#print(ma)
