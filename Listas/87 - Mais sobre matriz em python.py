#DECLARAÇÃO DE LISTAS E VARIÁVEIS NECESSÁRIAS:

fileira = [[0,0,0],[0,0,0],[0,0,0]]
somapar = 0
soma3coluna = 0
maior2coluna = 0

#PROCESSAMENTO:

for l in range (0,3):
    for c in range (0,3):
        fileira[l][c] = int(input(f"Digite um valor para {[l, c]}: "))

        if fileira[l][c] % 2 == 0:
            somapar += fileira[l][c]
        
        if c == 1 and fileira[l][c] > maior2coluna:
            maior2coluna = fileira[l][1]   

        if c == 2:
            soma3coluna += fileira[l][2]


#SAÍDA DE DADOS:
  
for item in range (0,3):
	print(fileira[item])

print(f"""Soma dos valores pares digitados: {somapar}
Soma dos números da terceira coluna: {soma3coluna}
O maior número da segunda coluna é {maior2coluna}""")
