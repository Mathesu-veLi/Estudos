jogador = {'nomeDoJogador': input('Nome do jogador: '),
           'partidasJogadas': int(input('Partidas jogadas: ')),
           'gols': [],}


for c in range(1, jogador['partidas jogadas'] + 1):
    jogador['gols'].append(int(input(f'Quantidade de gols feitos na partida {c}: ')))
    
jogador['totalDeGols'] = sum(jogador['gols'])

for k, v in jogador.items():
    print(f'{k.capitalize()} = {v}')
    
print(f'O jogador {jogador["nomeDoJogador"]} jogou {jogador["partidasJogadas"]} partidas')

for i, a in enumerate(jogador['gols']):
    print(f'    Na {i} partida, o jogador fez {a} gols')

print(f'No total, {jogador["nomeDoJogador"]} fez {jogador["totalDeGols"]}')