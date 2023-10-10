student_info = {'name': str(input('Nome do aluno: '))}
student_info['average'] = float(input(f"Média do {student_info['Nome']}: "))
if student_info['average'] > 7:
    student_info['situation'] = 'Aprovado'
else:
    student_info['situation'] = 'Reprovado'
for key, value in student_info.items():
    print(f'{key} é igual a {value}')
