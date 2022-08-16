#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input("Digite uma frase: ")).strip() .upper()
junto = frase.replace(" ","")
inverso = ""

for p in range(len(junto) - 1,-1, -1):
    inverso += junto[p] #Porque os colchetes? Inverter uma string? WTF??????

if inverso == junto:
    print("A frase {} é um palíndromo".format(junto))
else: 
    print("A frase {} não é um palíndromo".format(junto))