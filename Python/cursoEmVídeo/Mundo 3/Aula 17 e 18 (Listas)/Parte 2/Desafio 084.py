registered_persons = []
person_data = []
highest_weight = lowest_weight = 0

while True:
    person_data.append(input('Nome: '))
    person_data.append(float(input('Peso: ')))

    if len(registered_persons) == 0:
        highest_weight = person_data[1]
        lowest_weight = person_data[1]
    else:
        if person_data[1] > highest_weight:
            highest_weight = person_data[1]
        if person_data[1] < lowest_weight:
            lowest_weight = person_data[1]

    registered_persons.append(person_data[:])
    person_data.clear()

    to_continue = str(input('Deseja continuar? [S/N]: ')).lower()
    while to_continue not in 'sn':
        to_continue = str(
            input('Dados inválidos. Por favor digite S para continuar e N para parar: ')).lower()
    if 'n' in to_continue:
        break

print(f'Foram cadastradas {len(registered_persons)} pessoas')
print(f'O maiorPeso peso digitado foi {highest_weight}Kg de', end=' ')
for p in registered_persons:
    if p[1] == highest_weight:
        print(f'{p[0]}', end=' ')

print(f'\nO menorPeso peso digitado foi {lowest_weight}Kg de', end=' ')
for a in registered_persons:
    if a[1] == lowest_weight:
        print(f'{a[0]}', end=' ')
