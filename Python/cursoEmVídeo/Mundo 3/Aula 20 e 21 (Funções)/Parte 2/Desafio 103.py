def ficha(nomeDoJogador=0, númeroDeGols=0):
    if nomeDoJogador == '':
        nomeDoJogador = '<desconhecido>'
    if númeroDeGols.isnumeric() == False:
        númeroDeGols = 0
    print(f'O jogador {nomeDoJogador} fez {númeroDeGols} gols no campeonato')
        
nomeDoJogador = str(input('Nome do jogador: '))
númeroDeGols = str(input('Número de gols: '))
ficha(nomeDoJogador, númeroDeGols)