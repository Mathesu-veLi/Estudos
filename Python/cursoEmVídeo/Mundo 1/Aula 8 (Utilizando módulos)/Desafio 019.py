from random import choice


students = []
for student in range(1, 5):
    students.append(str(input(f'Digite o nome do {student}° aluno: ')))
print(f'O aluno escolhido foi..... {choice(students)}!!!!')