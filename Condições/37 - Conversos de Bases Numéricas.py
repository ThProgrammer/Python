#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

print('====== EXERCÍCIO 37 - Conversor de Bases Numéricas ======')
print('')

n = int(input("Digite um número inteiro: "))
print("")

print("""Escolha uma das bases para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL""")

escolha = int(input("Sua opção: "))

if escolha == 1:
    print("{} convertido para BINÁRIO é igual a {}.".format(n, bin(n)[2:]))

elif escolha == 2:
    print("{} convertido para OCTAL é igual a {}.".format(n, oct(n)[2:]))

elif escolha == 3:
    print("{} convertido para HEXADECIMAL é igual a {}.".format(n, hex(n)[2:]))

else:
    print("ERRO: Opção inválida, por favor tente novamente.")
