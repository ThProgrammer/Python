conta = str(input("Insira sua expressão: "))

if conta.count('(') == conta.count(')'):
    print("Sua expressão é valida.")

else:
    print("Sua expressão não é válida.")

print(conta.count("("))
print(conta.count(")"))
print(conta)