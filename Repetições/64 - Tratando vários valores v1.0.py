countv = 0
n = 0
soma = 0

while n != 999:
    n = int(input("Digite um valor: "))
    soma += n
    countv += 1 #Quantos valores foram digitados

print("Foram digitados {} valores e a soma de todos resulta em {}".format(countv-1, soma-999))

