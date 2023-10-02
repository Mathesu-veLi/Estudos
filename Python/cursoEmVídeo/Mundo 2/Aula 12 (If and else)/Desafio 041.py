from datetime import date


yearOfBirth = int(input('Qual o ano que você nasceu?: '))
age = date.today().year - yearOfBirth
 
print('Você esta na categoria ', end='')
if age <= 9:
    print('MIRIN')
elif age <= 12:
    print('INFANTIL')
elif age <= 18:
    print('JÚNIOR')
elif age <= 25:
    print('SÊNIOR')
else:
    print('MASTER')