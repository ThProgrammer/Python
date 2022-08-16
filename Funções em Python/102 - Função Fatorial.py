def fatorial (n, show = False):
    #Docstring:
    """
    --> Calcula o Fatorial de um Número.
    Parâmetro n = O número a ser calculado.
    Parâmetro show (opcional) = Mostra a conta do fatorial.
    return = O valor do Fatorial de um número n.
    """
    f = 1
    
    for i in range(n, 0, -1):
        if show: 
            print(i, end=" ")
            if i > 1: print("x", end=" ")
            else: print("=", end=" ")
        f *= i

    return f

#PROGRAMA PRINCIPAL
x = int(input("Insira um valor: "))
print(fatorial(x, show=True))