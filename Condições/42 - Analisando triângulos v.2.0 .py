# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais 
# ISÓSCELES: dois lados iguais
# ESCALENO: todos os lados diferentes

print('====== EXERCÍCIO 42 ======')
print('')

s1 = float(input('Digite o primeiro segmento: '))
s2 = float(input('Digite o segundo segmento: '))
s3 = float(input('Digite o terceiro segmento: '))

if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print ('Os segmentos acima podem formar um triângulo.')
    if s1 == s2 and s2 == s3:
        print('Os segmentos acima podem formar um triângulo EQUILÁTERO. ')
    elif s1 == s2 or s2 == s3 or s3 == s1:
        print('Os segmentos acima podem formar um triângulo ISÓSCELES. ')
    else:
        print('Os segmentos acima podem formar um triângulo ESCALENO.')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')