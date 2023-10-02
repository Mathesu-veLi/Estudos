from random import shuffle


students = []
for student in range(1, 5):
    students.append(str(input(f'Digite o nome do {student}° aluno: ')))
shuffle(students)

print(f'A ordem dos alunos escolhida foi: ', end='')
for student in students:
    print(student, end=' ')
