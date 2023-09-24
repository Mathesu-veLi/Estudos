from datetime import date

def voto(idade):
    if idade >= 18 and idade < 70:
        return 'OBRIGATÓRIO'
    elif idade >= 70 or idade >= 16 and idade < 18:
        return 'OPCIONAL'
    else:
        return 'NEGADO'


anoDeNascimento = int(input('Em que ano você nasceu?: '))
idade = date.today().year - anoDeNascimento
print(f'Seu voto é {voto(idade)}, pois você tem {idade} anos de idade')
