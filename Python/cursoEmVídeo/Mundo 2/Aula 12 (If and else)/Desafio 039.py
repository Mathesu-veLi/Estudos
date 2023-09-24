from datetime import date
gênero = str(input('Digite ao lado seu gênero (Feminino ou Masculino): \033[4;33m')).strip().capitalize()

if 'F' in gênero:
    print('\033[m\033[1;35mDesculpe! O alistamento é so para pessoas do sexo masculino\033[m')

elif 'M' in gênero:
    anoAtual = date.today().year
    anoDeNascimento = int(input('\033[mDigite aqui o ano do seu nascimento: '))
    idade = anoAtual - anoDeNascimento
    
    if idade == 18:
        print('Já está na hora de se alistar')
    elif idade > 18:
        diferençaEntreIdadeAtualE18Anos = idade - 18
        print(f'Já passou {diferençaEntreIdadeAtualE18Anos} anos do ano que você deveria se alistar')
        print(f'Seu alistamento foi, ou deveria ser em {anoAtual - diferençaEntreIdadeAtualE18Anos}')
    else:
        diferençaEntreIdadeAtualE18Anos = 18 - idade
        print('Ainda falta {} anos para o seu alistamento'.format(diferençaEntreIdadeAtualE18Anos))
        print('Seu alistamento será em {}'.format(anoAtual + diferençaEntreIdadeAtualE18Anos))
else:
    print('\033[m\033[1;31mAcho que você digitou seu gênero errado... Tente novamente digitando "Masculino" ou "Feminino"!\033[m')