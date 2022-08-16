def google (comando):
    return help (comando)

while True:
    comando = input("Insira um comando para receber ajuda (fim para parar): ")
    if comando in "FIMfimFim": break
    google(comando)
print("Até a proxima!")