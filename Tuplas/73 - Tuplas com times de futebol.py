times = ("América-MG", "Athlético-PR", "Atlético-GO", "Atlético-MG", "Avaí", "Botafogo", "Ceará SC", "Corinthians", "Coritiba", "Cuiabá", "Flamengo", "Fluminense", "Fortaleza", "Goiás", "Internacional", "Juventude", "Palmeiras", "Bragantino", "Santos", "São Paulo")
print(f"Os 5 primeiros colocados da tabela são {times[0:5]}")
print(f"Os 4 últimos colocados da tabela são {times[16:20]}")
print(f"Os times organizados em ordem alfabéticas são {sorted(times)}")
print(f"O são paulo está na colocação: ", times.index("São Paulo")+1) 
