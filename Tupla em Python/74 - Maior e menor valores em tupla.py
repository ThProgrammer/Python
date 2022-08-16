from random import randrange
maior = 0
menor = 0
count = 0
item = 0

na = (randrange(0,10), randrange(0,10), randrange(0,10), randrange(0,10), randrange (0,10))

for i in range (0, len(na)):

    if na [i] >= maior:
        maior = na [i]

        if na [0] >= menor and count == 0:
            menor = na [0]
            count += 1

    if na [i] < menor:
        menor = na [i]   

print(na)
print(maior)
print(menor)