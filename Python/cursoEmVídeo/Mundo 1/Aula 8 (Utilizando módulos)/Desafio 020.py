from random import shuffle


alunos = []
for c in range(1, 5):
    alunos.append(str(input(f'Digite o nome do {c}° aluno: ')))
shuffle(alunos)
print(f'A ordem dos alunos escolhida foi: {alunos}')