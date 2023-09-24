dadosDoAluno = []
while True:
    nome = input('Digite o nome do aluno: ')
    primeiraNota = float(input(f"Digite a 1° nota de {nome}: "))
    segundaNota = float(input(f"Digite a 2° nota de {nome}: "))
    média = (primeiraNota + segundaNota) / 2
    dadosDoAluno.append([nome, [primeiraNota, segundaNota], média])
    continuar = str(input('Deseja continuar? [S/N]: ')).lower()
    while continuar not in 'sn':
        continuar = str(input('Dados inválidos. Por favor digite S para continuar e N para parar: '))
    if 'n' in continuar:
        break

print(f'\n{"No.":<4}{"Nome":<10}{"Média":>8}')
for i, a in enumerate(dadosDoAluno):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

aluno = 0
while aluno != 999:
    aluno = int(input('\nDeseja ver as notas de qual aluno? (999 interrompe): '))
    if aluno <= len(dadosDoAluno) - 1:
        print(f'Notas de {dadosDoAluno[aluno][0]} são {dadosDoAluno[aluno][1]}')