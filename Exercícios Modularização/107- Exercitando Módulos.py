from ex107 import moeda
#ex107 é meu pacote e moeda é meu módulo, onde estão minhas funções.

number = float(input("Digite um número: "))
print(f"A metade de {number} é {moeda.metade(number)}")
print(f"O dobro de {number} é {moeda.dobro(number)}")
print(f"Aumentando 10% de {number}, temos {moeda.aumentar(number, 10)}")
print(f"Diminuindo 13% de {number}, temos {moeda.diminuir(number, 13)}")