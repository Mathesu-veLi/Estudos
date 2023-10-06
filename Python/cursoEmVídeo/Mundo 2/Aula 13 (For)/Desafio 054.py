from datetime import date


people_of_legal_age = 0
underage_people = 0

for iterator in range(1, 8):
    year_of_birth = int(input(f'Digite o ano de nascimento da {iterator}° pessoa: '))
    if year_of_birth <= date.today().year - 18:
        people_of_legal_age += 1
    else:
        underage_people += 1
        
print(f'{people_of_legal_age} pessoas são maior de idade')
print(f'{underage_people} pessoas são menor de idade')