from random import choice


students = []
for iterator in range(1, 5):
    students.append(str(input(f'Digite o nome do {iterator}° aluno: ')))

print(f'O aluno escolhido foi..... {choice(students)}!')
