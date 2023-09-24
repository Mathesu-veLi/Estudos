jogadoresCadastrados = []
while True:
    jogador = {'nomeDoJogador': input('Nome do jogador: '),
            'partidasJogadas': int(input('Partidas jogadas: ')),
            'gols': []}
    for c in range(1, jogador['partidasJogadas'] + 1):
        jogador['gols'].append(int(input(f'Quantidade de gols feitos na partida {c}: ')))
    jogador['totalDeGols'] = sum(jogador['gols'])
    jogadoresCadastrados.append(jogador.copy())
    jogador.clear()
    while True:
        cont = input('Deseja continuar? [S/N]: ')
        if cont in 'SsNn':
            break
        else:
            print('Digite "S" para continuar e "N" para parar')
    if cont in 'Nn':
        break
print(f'\n{"cod":<4}{"nome":<10}{"gols":>8}{"total":>17}')

for n, a in enumerate(jogadoresCadastrados):
    print(f'{n:<4}{a["nomeDoJogador"]:<14}{str(a["gols"]):<16}{str(a["totalDeGols"]):<3}')
print('-' * 39)
while True:
    while True:    
        códigoDoJogador = int(input('Digite o código do jogador para ver os detalhes de seu aprimoramento (999 para parar): '))
        if códigoDoJogador > len(jogadoresCadastrados) and códigoDoJogador != 999:
            print('ERRO! O código digitado não existe, tente novamente!')
        else:
            if códigoDoJogador == 999:
                break
            for k, v in jogadoresCadastrados[códigoDoJogador].items():
                if k == 'nomeDoJogador':
                    print('Detalhes de aprimoramento do jogador ', v, ':')
                if k == 'gols':
                    for a, j in enumerate(v):
                        print(f'    No jogo {a} fez {j} gols')    