def leiaDinheiro(question = "Insira um preço: "):
    vermelho = False
    while True:   
        try: dinheiro = str(input(question)).replace(",",".").strip()
        except KeyboardInterrupt: 
            print(red("Dados não informados."))
            return
        
        try:
            return(float(dinheiro))
        except: 
            if vermelho == False:
                question = red(f"ERRO! {question}")
                vermelho = True

#
def leiaInt(question = "Insira um número inteiro: "):
    vermelho = False
    while True:
        try: 
            number = int(input(question))
            return number
        
        except (ValueError, TypeError):
            if vermelho == False:
                question = red(f"ERRO! {question}")
                vermelho = True
        
        except KeyboardInterrupt:  
            print(red("Número não informado"))
            return
            

def leiaFloat(question = "Insira um número flutuante: "):
    vermelho = False
    while True:
        try: number = str(input(question)).replace(",",".")
        except KeyboardInterrupt: 
            print(red("Número não informados"))
            return

        try: return float(number)
        except: 
            if vermelho == False:
                question = red(f"ERRO! {question}")
                vermelho = True
#

def leiaNumero(pergunta = "Insira um número: "):
    vermelho = False
    while True:
        try: numero = str(input(pergunta)).replace(",",".")
        except KeyboardInterrupt: 
            print(red("Número não informado"))
            return

        if numero.find(".") != -1:
            try: return float(numero)
            except: 
                if vermelho == False:
                    pergunta = red(f"ERRO! {pergunta}")
                    vermelho = True
        else:
            try: return int(numero)
            except:
                if vermelho == False:    
                    pergunta = red(f"ERRO! {pergunta}")
                    vermelho = True
            

def red(msg = "Erro"):
    return (f"\033[031m{msg}\033[m") #\033[0;31m \033[m == Código pra deixar a linha VERMELHA.
#LeiaInt Versões Anteriores.
"""def leiaInt1.0(question = "Insira um número inteiro: "):
#FALTA O DOCSTRING!!!!!!!
    number = str(input(question))
    while True:
        if number.isnumeric(): return int(number)
        else:
            number = str(input(f"\033[0;31mERRO! {question} \033[m")) #\033[0;31m \033[m == Código pra deixar a linha VERMELHA.

def leiaInt com tratamento de erro(question = "Insira um número inteiro: "):
    from ex111.utilidadescev.dado.dado import red
    try: number = str(input(question))
    except KeyboardInterrupt: return ("Dados não informados")
    
    while True:
        try: 
            return int(number)
        except: 
            try: 
                number = str(input(red(f"ERRO! {question}"))) 
            except KeyboardInterrupt: return red("Dados não informados")"""