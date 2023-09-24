informaçõesDoAluno = {'Nome': input('Nome do aluno: ')}
informaçõesDoAluno['Média'] = float(input(f"Média do {informaçõesDoAluno['Nome']}: "))
if informaçõesDoAluno['Média'] > 7:
    informaçõesDoAluno['Situação'] = 'Aprovado'
else:
    informaçõesDoAluno['Situação'] = 'Reprovado'
for k, v in informaçõesDoAluno.items():
    print(f'{k} é igual a {v}')