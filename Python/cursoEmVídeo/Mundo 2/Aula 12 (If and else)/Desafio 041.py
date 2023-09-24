from datetime import date
anoDeNascimento = int(input('Qual o ano que você nasceu?: '))
idade = date.today().year - anoDeNascimento
if idade <= 9:
    print('Você esta na categoria MIRIN')
elif idade <= 12:
    print('Você esta na categoria INFANTIL')
elif idade <= 18:
    print('Você está na categoria JÚNIOR')
elif idade <= 25:
    print('Você esta na categoria SÊNIOR')
else:
    print('Você esta na categoria MASTER')