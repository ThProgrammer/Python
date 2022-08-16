def leiaInt(question):
#FALTA O DOCSTRING!!!!!!!
    number = str(input(question))
    while True:
        if number.isnumeric():
            number = int(number)
            return number
        else:
            number = str(input("\033[0;31mERRO! Por favor, insira um valor inteiro: \033[m")) #\033[0;31m \033[m == Código pra deixar a linha VERMELHA.
    

#PROGRAMA PRINCIPAL
n = leiaInt("Digite um número por favor: ")
print(n)