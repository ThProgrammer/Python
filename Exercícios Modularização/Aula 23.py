try:  #Tente fazer esse bloco
    a = int(input("Dividendo: "))
    b = int(input("Divisor: "))
    r = a/b

except (ValueError, TypeError): #Se deu errado, executa esse bloco
    print("Tivemos um problema com o tipo de dados que você digitou")
    
#Um try pode ter vários except
except ZeroDivisionError:
    print("Divisão por zero não é aceita! :(")

except KeyboardInterrupt:
    print("Não foram inseridos dados.")

else: #Agora se deu certo, execute esse bloco.
    print(r)

finally: #Independente se o programa der certo ou não, depois de tudo, esse bloco acontecerá
    print("Volte sempre! Muito Obrigado!")