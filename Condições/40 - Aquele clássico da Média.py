#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

print('====== EXERCÍCIO 40 ======')
print('Olá, estou aqui para te ajudar a calcular sua média, digite suas notas e direi sua situação! :)')
print('')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2
print('')
print('Com as notas {:.1f} e {:.1f} sua média é {:.1f}'.format(n1, n2, m))

#(:.1f)  significa formatado a 1 casa decimal, ou uma casa depois do ./,

if m >= 7:
    print('Você está aprovado! :)')
elif m < 5:
    print('Você está reprovado, sinto muito :(')
else:
    print('Você está de recuperação, ainda tem salvação!')