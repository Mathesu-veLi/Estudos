registred_footballers = []

while True:
    footballer = {'name': str(input('Nome do jogador: ')),
                  'matches played': int(input('Partidas jogadas: ')),
                  'goals': []}

    for iterator in range(1, footballer['matches played'] + 1):
        footballer['goals'].append(
            int(input(f'Quantidade de gols feitos na partida {iterator}: ')))
    footballer['total_goals'] = sum(footballer['goals'])

    registred_footballers.append(footballer.copy())
    footballer.clear()

    while True:
        to_continue = str(input('Deseja continuar? [S/N]: ')).lower()
        if to_continue in 'sn':
            break
        else:
            print('Digite "S" para continuar e "N" para parar')

    if to_continue in 'n':
        break

print(f'\n{"cod": <4}{"nome": <10}{"gols": >8}{"total": >17}')

for iterator, footballer in enumerate(registred_footballers):
    print(f'{iterator: <4}{footballer["name"]: <14}{str(footballer["goals"]): <16}{str(footballer["total_goals"]): <3}')

print('-' * 39)
while True:
    footballer_code = int(input(
        'Digite o código do jogador para ver os detalhes de seu aprimoramento (999 para parar): '))

    if (footballer_code > len(registred_footballers)) and footballer_code != 999:
        print('ERRO! O código digitado não existe, tente novamente!')
    else:
        if footballer_code == 999:
            break

        for key, value in registred_footballers[footballer_code].items():
            if key == 'name':
                print('Detalhes de aprimoramento do jogador ', value, ':')

            if key == 'goals':
                for iterator, goal_amount in enumerate(value):
                    print(f'    No jogo {iterator} fez {goal_amount} gols')
