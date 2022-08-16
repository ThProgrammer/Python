import urllib
import urllib.request

site = (input("Insira o site: "))

for t in range(0, 1):
    try:
        site = f"http://www.{site}.com"
        acesssite = urllib.request.urlopen(site)
        print(f"Consegui acessar {site}")
    except urllib.error.URLError: 
        site += ".br"
        print(f"Não consegui acessar {site}!")