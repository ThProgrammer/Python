#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print("====== EXERCÍCIO 47 - Contagem de Pares ======")
print("")
print("Aqui estão todos os números pares entre 1 e 50:")
print("")

for p in range(2, 51, 2):
    print(p) 


#O PROGRAMA ABAIXO APESAR DE FUNCIONAR, FAZIA O LAÇO P O DOBRO DE VEZES QUE O NECESSÁRIO.

#for p in range (1, 51):
#    if p%2 == 0: #o if dentro do laço consegue pegar todos os valores de p, se estiver fora, só vai pegar o ultimo valor (no caso 50)
#        print(p, end=" ") #pq end faz o que faz? / pq end???

