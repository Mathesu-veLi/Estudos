averageBetweenAges = olderAgeAmongMen = womenOverTwentyYearsOld = 0
nameOfTheOldestMan = ''

for quantifier in range(1, 5):
    print(f'\n {quantifier}° pessoa')
    
    nameOfPerson = str(input('Nome: ')).strip().capitalize()
    ageOfPerson = int(input('Idade: '))
    
    while True:
        genderOfPerson = str(input('Gênero [M/F]: ')).lower().strip()
        
        if 'm' in genderOfPerson or 'f' in genderOfPerson: 
            break
        print('Digite M para o gênero masculino e F para o gênero feminino')
    
    averageBetweenAges += ageOfPerson
    
    if 'm' in genderOfPerson and (quantifier == 1 or ageOfPerson > olderAgeAmongMen):
        olderAgeAmongMen = ageOfPerson
        nameOfTheOldestMan = nameOfPerson
    
    if 'f' in genderOfPerson and ageOfPerson > 20:
        womenOverTwentyYearsOld += 1

averageBetweenAges /= 4
print(f'A media da idade do grupo é de {averageBetweenAges:.2f} anos')
print(f'O homem mais velho tem {olderAgeAmongMen} anos e o nome dele é {nameOfTheOldestMan}')
print(f'E ao todo, são {womenOverTwentyYearsOld} mulheres com menos de 20 anos')