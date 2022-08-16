extenso =("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

n = int(input("Insira um número entre 0 e 20: "))


while n < 0 or n > 20: #Validação de dados.
    n = int(input("Por favor, insira um número entre 0 e 20: "))

print (f"O número digitado escrito por extenso é {extenso[n]}.")


