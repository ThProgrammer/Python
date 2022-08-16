opcao = 0

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))

while opcao != 5:
    opcao = int(input("""Escolha uma das opções do menu
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
"""))

    if opcao == 1:
        print("""{} + {} = {}""".format(n1, n2, n1 + n2))

    elif opcao == 2:
        print("{} x {} = {}".format(n1, n2, n1 * n2))
        
    elif opcao == 3:
        if n1>n2:
            print("O maior valor é {}".format(n1))
        else:
            print("O maior valor é {}".format(n2))
    elif opcao == 4:
        n1 = int(input("Digite um valor: "))
        n2 = int(input("Digite outro valor: "))


print(
"""Até a próxima!""")
        