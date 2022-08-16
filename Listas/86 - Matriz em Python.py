#fileira = [[[],[],[]], [[],[],[]], [[],[],[]]]
fileira = [[0,0,0],[0,0,0],[0,0,0]]


for l in range (0,3):
    for c in range (0,3):
        fileira[l][c] = int(input(f"Digite um valor para {[l, c]}: "))


for item in range (0,3):
	print(fileira[item])
    
    