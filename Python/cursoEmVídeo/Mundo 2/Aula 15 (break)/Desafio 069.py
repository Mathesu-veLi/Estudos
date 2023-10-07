order = 1
women_under_twenty = people_over_eighteen = registered_men = registered_people = 0

while True:
    age = int(input(f'Digite a idade da {order}° pessoa: '))
    order += 1

    while True:
        gender = str(input('Digite agora o sexo dela [M/F]: ')).upper()
        if gender in 'mf':
            break
        print('Digite M para masculino e F para feminino!')

    if age < 20 and gender == 'F':
        women_under_twenty += 1

    if gender == 'M':
        registered_men += 1

    if age >= 18:
        people_over_eighteen += 1

    registered_people += 1

    while True:
        to_continue = str(
            input('Deseja cadastrar mais alguma pessoa? [S/N]: ')).lower()
        if to_continue in 'ns':
            break
        print('Digite S se deseja cadastrar mais alguém ou N caso não')
    if 'n' in to_continue:
        break

print(f'''Foram cadastradas {registered_people} pessoas
      {people_over_eighteen} tem mais de 18 anos
      {women_under_twenty} são mulheres abaixo dos 20 anos
      {registered_men} são homens''')
