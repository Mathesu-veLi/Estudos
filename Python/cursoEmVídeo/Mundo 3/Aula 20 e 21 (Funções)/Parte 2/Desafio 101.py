from datetime import date
from modules import check_voting_obligation


year_of_birth = int(input('Em que ano você nasceu?: '))
age = date.today().year - year_of_birth

print(f'Seu voto é {check_voting_obligation(
    age)}, pois você tem {age} anos de idade')
