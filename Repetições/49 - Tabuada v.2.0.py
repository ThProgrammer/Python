#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for

print("====== INÍCIO ======")

n = int(input("Digite um número: "))

for t in range (1, 11):
    print("{}x{} igual a {}".format(n, t, n*t))




