def contador (start, end, step):
    from time import sleep #Não esqueça de verificar se flush = True é necessário
    
    if step == 0:
        step = 1
    elif step < 0:
        step *= -1

    print(f"\nContagem de {start} até {end} de {step} em {step}")
    
    if start > end:
        if step > 0: #Se o inicio for maior que o fim, e o passo for maior que zero...
            step = step*-1 #passaremos o passo para negativo, para que a contagem regressiva aconteça

        while start >= end: #Por algum motivo não consegui usar while inicio != fim: inicio += passo, ele ficava somando infinitamente e nunca igualava, acredito ser pela maneira que os parâmetros foram enviados.
            print(start, end=" ", flush=True) #Atualização: Não acontece mais. Não sei porquê
            sleep(0.3)
            start += step

    else:
        while start <= end: #Por algum motivo não consegui usar while inicio != fim: inicio += passo, ele ficava somando infinitamente e nunca igualava, acredito ser pela maneira que os parâmetros foram enviados.
            print(start, end=" ", flush=True) #Atualização: Não acontece mais. Não sei porquê
            sleep(0.3)
            start += step
    print("FIM!")


#PROGRAMA PRINCIPAL
contador(1, 10, 1)
contador(10, 0, 2)
contador(start = int(input("Insira o início: ")), end = int(input("Insira o fim: ")), step = int(input("Insira o passo: "))) 