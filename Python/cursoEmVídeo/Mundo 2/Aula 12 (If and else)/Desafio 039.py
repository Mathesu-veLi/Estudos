from datetime import date



while True:
    gender = str(input('Digite ao lado seu gênero (Feminino ou Masculino): ')).strip().capitalize()
    
    if 'F' in gender:
        print('Desculpe! O alistamento é so para pessoas do sexo masculino')
        break

    elif 'M' in gender:
        currentYear = date.today().year
        yearOfBirth = int(input('Digite aqui o ano do seu nascimento: '))
        age = currentYear - yearOfBirth
        
        if age == 18:
            print('Já está na hora de se alistar')
        elif age > 18:
            differenceBetweenCurrentAgeAnd18Years = age - 18
            print(f'Já passou {differenceBetweenCurrentAgeAnd18Years} anos do ano que você deveria se alistar')
            print(f'Seu alistamento foi, ou deveria ser em {currentYear - differenceBetweenCurrentAgeAnd18Years}')
        else:
            differenceBetweenCurrentAgeAnd18Years = 18 - age
            print(f'Ainda falta {differenceBetweenCurrentAgeAnd18Years} anos para o seu alistamento')
            print(f'Seu alistamento será em {currentYear + differenceBetweenCurrentAgeAnd18Years}')
        break
    
    else:
        print('Acho que você digitou seu gênero errado... Tente novamente digitando "Masculino" ou "Feminino"!')