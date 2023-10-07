value_to_be_withdrawn = int(input('Qual vai ser o valor sacado?: R$'))
total_value = value_to_be_withdrawn
ballots = 20
total_ballots = 0

while True:
    if total_value >= ballots:
        total_value -= ballots
        total_ballots += 1
        
    else:
        if total_ballots > 0:
            print(f'Você sacou {total_ballots} cédulas de R${ballots}')
        
        match(ballots):
            case 50:
                ballots = 20
            case 20:
                ballots = 10
            case 10:
                ballots = 1
        
        total_ballots = 0
        break