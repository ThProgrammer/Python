import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com')
    print(f"Consegui acessar!")
    print(site.read())
except urllib.error.URLError: 
    print(f"Não consegui acessar {site}!")