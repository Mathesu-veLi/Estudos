player = {'name': input('Nome do jogador: '),
          'matches played': int(input('Partidas jogadas: ')),
          'goals': [], }


for match_number in range(1, player['partidas jogadas'] + 1):
    player['goals'].append(
        int(input(f'Quantidade de gols feitos na partida {match_number}: ')))

player['total goals'] = sum(player['goals'])

for key, value in player.items():
    print(f'{key.capitalize()} = {value}')

print(f'O jogador {player["name"]} jogou {player["matches played"]} partidas')

for match_number, match_goals in enumerate(player['goals']):
    print(f'Na {match_number} partida, o jogador fez {match_goals} gols')

print(f'No total, {player["name"]} fez {player["total goals"]}')
