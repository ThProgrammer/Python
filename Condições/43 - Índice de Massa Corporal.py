#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

#– IMC abaixo de 18,5: Abaixo do Peso

#– Entre 18,5 e 25: Peso Ideal

#– 25 até 30: Sobrepeso

#– 30 até 40: Obesidade

#– Acima de 40: Obesidade Mórbida

print("====== EXERCÍCIO 43 - IMC ======")
print("")

p = float(input("Qual seu peso? "))
a = float(input("Qual sua altura? "))
imc = p / a**2
print("")
print("O seu IMC é de {:.1f}".format(imc))
print("")
if imc < 18.5:
    print("Você está ABAIXO DO PESO.")
elif 18.5 < imc >25:
    print("Você está no PESO IDEAL.")
elif 25 <= imc < 30:
    print("Você está em SOBREPESO.")
elif 30 <= imc <40:
    print("Você está em OBESIDADE.")
else:
    print("Você está em OBESIDADE MÓRBIDA.")
