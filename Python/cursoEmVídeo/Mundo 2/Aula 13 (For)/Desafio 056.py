average_between_ages = older_age_among_men = women_over_twenty_years_old = 0
name_of_the_oldest_man = ''

for iterator in range(1, 5):
    print(f'\n {iterator}° pessoa')

    name_of_person = str(input('Nome: ')).strip().capitalize()
    age_of_person = int(input('Idade: '))

    while True:
        gender_of_person = str(input('Gênero [M/F]: ')).lower().strip()

        if gender_of_person in 'mf':
            break
        print('Digite M para o gênero masculino e F para o gênero feminino')

    average_between_ages += age_of_person

    if 'm' in gender_of_person and (iterator == 1 or age_of_person > older_age_among_men):
        older_age_among_men = age_of_person
        name_of_the_oldest_man = name_of_person

    if 'f' in gender_of_person and age_of_person > 20:
        women_over_twenty_years_old += 1

average_between_ages /= 4
print(f'A media da idade do grupo é de {average_between_ages:.2f} anos')
print(
    f'O homem mais velho tem {older_age_among_men} anos e o nome dele é {name_of_the_oldest_man}')
print(
    f'E ao todo, são {women_over_twenty_years_old} mulheres com menos de 20 anos')
