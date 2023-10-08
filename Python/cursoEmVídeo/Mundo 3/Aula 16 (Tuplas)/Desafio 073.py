brazilian_championship_series_A = 'Palmeiras', 'Corinthians', 'Atlético-MG', 'Fluminense', 'Atlético-PR', 'Internacional', 'São Paulo', 'Santos', 'Flamengo', 'Botafogo', 'Bragantino', 'Goiás', 'Cuiabá', 'Coritiba', 'América-MG', 'Avaí', 'Ceará SC', 'Atlético-GO', 'Juventude', 'Fortaleza'

print(f'Os cinco primeiro colocados foram o {brazilian_championship_series_A[0:5]}')
print(f'Os quatro últimos foram o {brazilian_championship_series_A[-4:]}')
print(f'Os times da serie A em ordem alfabética fica:\n{sorted(brazilian_championship_series_A)}')
print(f'O Flamengo está na {brazilian_championship_series_A.index("Flamengo") + 1}ª posição')