from random import choice


alunos = []
for c in range(1, 5):
    alunos.append(str(input(f'Digite o nome do {c}° aluno: ')))
print(f'O aluno escolhido foi..... {choice(alunos)}!!!!')