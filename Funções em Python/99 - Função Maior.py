from time import sleep

def maior(* n):
    b = sorted(n) #Coloquei a tupla organizada em outra tupla, pois sorted não a altera, só organiza pra exibição

    print(f"Foram informados os valores", end= " ") 
    for i in n:
        print(i, end=" ", flush=True)
        sleep(0.3)
    print(f"\n{len(n)} valores ao todo")
    print(f"O maior valor informado foi {b[len(b)-1]}")


#Programa Principal:
maior(5, 3, 9, 7)