v = float(input('Qual a velocidade que seu carro está? '))
vm = (v-80)*7

if v> 80:
    print('Você foi multado no valor de {} reais, por excesso de velocidade.'.format(vm))

else:
    print('Você está dentro da velocidade permitida, continue assim!')
