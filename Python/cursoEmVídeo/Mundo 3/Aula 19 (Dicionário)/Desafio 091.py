from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'Jogador1': randint(1, 6), 'Jogador2': randint(1, 6), 'Jogador3': randint(1, 6), 'Jogador4': randint(1, 6)}

for k, v in jogadores.items():
    print(f'O {k.capitalize()} tirou {v} no dado')
    sleep(0.5)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for p, v in enumerate(ranking):
    print(f'{p+1}° lugar: {v[0]} com {v[1]}')