serieA = 'Palmeiras', 'Corinthians', 'Atlético-MG', 'Fluminense', 'Atlético-PR', 'Internacional', 'São Paulo', 'Santos', 'Flamengo', 'Botafogo', 'Bragantino', 'Goiás', 'Cuiabá', 'Coritiba', 'América-MG', 'Avaí', 'Ceará SC', 'Atlético-GO', 'Juventude', 'Fortaleza'
print(f'Os cinco primeiro colocados foram o {serieA[0:5]}')
print(f'Os quatro últimos foram o {serieA[-4:]}')
print(f'Os times da serie A em ordem alfabética fica:\n{sorted(serieA)}')
a = serieA.index('Flamengo') + 1
print(f'O Flamengo está na {a}ª posição')