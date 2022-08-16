from random import randrange
from time import sleep

countt = 1
numpc = randrange(1,11)

print("Vou pensar num número de 1 a 10!")
sleep(1)

numuser = int(input("Pensei! Você consegue adivnhar? "))

while numuser != numpc:
    countt += 1
    numuser = int(input("Errou! Tenta de novo! Qual número pensei? "))
print("""
Isso! Meu número era o {}! 
Você acertou na {}° tentativa.""".format(numpc, countt))
