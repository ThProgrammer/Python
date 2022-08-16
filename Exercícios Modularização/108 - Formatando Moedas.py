from ex108 import moeda
#ex108 é meu pacote e moeda é meu módulo, onde estão minhas funções.

number = float(input("Digite um número: R$"))
print(f"A metade de {moeda.format(number)} é {moeda.format(moeda.metade(number))}")
print(f"O dobro de {moeda.format(number)} é {moeda.format(moeda.dobro(number))}")
print(f"Aumentando 10% de {moeda.format(number)} , temos {moeda.format(moeda.aumentar(number, 10))}")
print(f"Diminuindo 13% de {moeda.format(number)} , temos {moeda.format(moeda.diminuir(number, 13))}")