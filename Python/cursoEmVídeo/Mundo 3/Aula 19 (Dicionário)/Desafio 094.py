registered_persons = []
average = []
registered_women_names = []
peaple_names_over_age = []

while True:
    personal_info = {'name': str(input('Qual o nome?: ')),
                     'gender': str(input('Qual o sexo? [M/F]: ')),
                     'age': int(input('Qual a idade?: '))}

    registered_persons.append(personal_info.copy())
    personal_info.clear()

    to_continue = str(input('Deseja continuar? [S/N]: ')).lower()
    while to_continue not in 'sn':
        to_continue = str(
            input('Dados inválidos. Por favor digite S para continuar e N para parar: ')).lower()

    if 'n' in to_continue:
        break

print(f'Foram cadastradas {len(registered_persons)} pessoas')

for person in registered_persons:
    for key, value in person.items():
        if key == 'age':
            average.append(value)
        if key == 'gender':
            if value == 'F':
                for second_key, second_value in person.items():
                    if second_key == 'name':
                        registered_women_names.append(second_value)

average_age = sum(average) / len(average)

for person in registered_persons:
    for key, value in person.items():
        if key == 'age':
            if value > average_age:
                peaple_names_over_age.append(person.copy())

print(f'A média da idade das pessoas cadastradas é de {average_age}')

print('O nome das mulheres cadastradas é: ')
for woman in registered_women_names:
    print(f'    {woman}')

print('O nome das pessoas com idade acima da média é:')
for person in peaple_names_over_age:
    print(f'    {person}')
