from datetime import date


peopleOfLegalAge = 0
underagePeople = 0

for c in range(1, 8):
    yearOfBirth = int(input(f'Digite o ano de nascimento da {c}° pessoa: '))
    if yearOfBirth <= date.today().year - 18:
        peopleOfLegalAge += 1
    else:
        underagePeople += 1
        
print(f'{peopleOfLegalAge} pessoas são maior de idade')
print(f'{underagePeople} pessoas são menor de idade')