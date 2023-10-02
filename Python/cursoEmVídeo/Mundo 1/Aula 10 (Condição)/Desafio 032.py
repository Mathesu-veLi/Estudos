from datetime import date


year = int(input('Digite um ano e saiba se ele é bissexto ou não! Coloque 0 para analisar o ano atual: '))

if year == 0:
    year = date.today().year
elif year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
    print(f'O ano {year} é bissexto')
else:
    print(f'O ano {year} não é bissexto')