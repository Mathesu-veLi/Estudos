from random import randint
from time import sleep
from operator import itemgetter

players = {
    'player 1': randint(1, 6),
    'player 2': randint(1, 6),
    'player 3': randint(1, 6),
    'player 4': randint(1, 6)
}

for key, value in players.items():
    print(f'O {key.capitalize()} tirou {value} no dado')
    sleep(0.5)

ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
print()
for position, value in enumerate(ranking):
    print(f'{position+1}° lugar: {value[0]} com {value[1]}')
