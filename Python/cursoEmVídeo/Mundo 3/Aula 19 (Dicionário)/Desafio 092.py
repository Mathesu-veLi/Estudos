from datetime import datetime as date

employee_info = {'name': input('Qual seu nome?: '),
                 'birth year': int(input('Em qual ano você nasceu?: ')),
                 'age': date.now().year,
                 'workbook number': input('Digite o número de sua carteira de trabalho (0 se não tem): ')}
employee_info['age'] = employee_info['age'] - employee_info['birth year']

if employee_info['workbook number'] != "0":
    employee_info['year hired'] = int(
        input('Em que ano você foi contratado?: '))
    employee_info['salary'] = float(input('Qual seu salário?: R$'))
    employee_info['retirement'] = (
        employee_info['age'] + employee_info['year hired'] + 20) - date.now().year

for key, value in employee_info.items():
    print(f'{key.capitalize()} recebe {value}')
