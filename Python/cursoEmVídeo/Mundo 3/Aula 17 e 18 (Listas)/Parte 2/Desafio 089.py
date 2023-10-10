student_data = []

while True:
    name = input('Digite o nome do aluno: ')
    first_grade = float(input(f"Digite a 1° nota de {name}: "))
    second_grade = float(input(f"Digite a 2° nota de {name}: "))
    average = (first_grade + second_grade) / 2

    student_data.append([name, [first_grade, second_grade], average])

    to_continue = str(input('Deseja continuar? [S/N]: ')).lower()
    while to_continue not in 'sn':
        to_continue = str(
            input('Dados inválidos. Por favor digite S para continuar e N para parar: '))
    if 'n' in to_continue:
        break

print(f'\n{"No.": <4}{"Nome": <10}{"Média": >8}')
for iterator, student in enumerate(student_data):
    print(f'{iterator: <4}{student[0]: <10}{student[2]: >8.1f}')

while True:
    student = int(
        input('\nDeseja ver as notas de qual aluno? (999 interrompe): '))
    if student == 999:
        break
    if student <= len(student_data) - 1:
        print(f'Notas de {student_data[student][0]} são {
              student_data[student][1]}')
