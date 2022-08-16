#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício
#indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

print("""    ====== EXERCÍCIO 46 ====== 
PREPAREM-SE PARA OS FOGOS DE ARTIFÍFICO
        QUE COMECE A CONTAGEM""")

for cr in range(10, -1, -1):
    print(cr)
    sleep(1)
print("BOOOOOOOMMMM")
sleep(1)
print("POW POW")
sleep(1)
print("FIOOOOOOOOON")
sleep(1)
print("PAAAAAA!")