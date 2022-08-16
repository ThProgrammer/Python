#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão.

print("====== 51 - Progressão Aritmética ======")
print("")
print("=== 10 termos de uma PA ===")
print("")

pt = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
dt = pt + (10-1)*r+r

for pa in range (pt, dt, r):
    print("{}".format(pa), end=' -> ')

print("FIM.")
