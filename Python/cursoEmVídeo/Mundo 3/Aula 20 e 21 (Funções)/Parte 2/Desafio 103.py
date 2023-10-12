from modules import player_sheet


footballer = {
    'name': str(input('Nome do jogador: ')),
    'number of goals': int(input('Número de gols: '))
}

player_sheet(footballer['name'], footballer['number of goals'])
