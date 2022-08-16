fileira = [[],[],[]]
#fileira = [[0,0,0][0,0,0],[0,0,0]]
fileira1 = [0,0,0]
fileira2 = [0,0,0]
fileira3 = [0,0,0]

for c in range (0,3):
    fileira1[c] = (int(input(f"Digite um valor para {[c]}: ")))

fileira.append(fileira1[:])

for c in range (0,3):
    fileira2[c] = (int(input(f"Digite um valor para {[c]}: ")))

fileira.append(fileira2[:])

for c in range (0,3):
    fileira3[c] = (int(input(f"Digite um valor para {[c]}: ")))

fileira.append(fileira3[:])

for item in range (0,3):
	print(fileira[item])