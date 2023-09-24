from random import randint
from time import sleep


conjuntoDeNúmero = []
jogos = []
quantidadeDeJogos = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(quantidadeDeJogos):
    for c in range(6):
        númeroAleatório = randint(1, 60)
        if númeroAleatório not in conjuntoDeNúmero:
            conjuntoDeNúmero.append(númeroAleatório)
    conjuntoDeNúmero.sort()
    jogos.append(conjuntoDeNúmero[:])
    conjuntoDeNúmero.clear()
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(0.5)
print(f'{"<" * 4} Boa sorte! {">" * 4}')