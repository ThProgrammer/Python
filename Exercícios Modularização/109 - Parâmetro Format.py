from ex109 import moeda
#ex109 é meu pacote e moeda é meu módulo, onde estão minhas funções.

number = float(input("Digite um número: "))
print(f"A metade de {moeda.output(number)} é {moeda.metade(number, True)}")
print(f"O dobro de {moeda.output(number)} é {moeda.dobro(number, True)}")
print(f"Aumentando 10% de {number} temos {moeda.aumentar(number, 10, True)}")
print(f"Diminuindo 13% de {number} temos {moeda.diminuir(number, 13, True)}")