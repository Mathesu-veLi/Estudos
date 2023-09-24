pessoasCadastradas = []
dadosDaPessoa = []
maiorPeso = menorPeso = 0
while True:
    dadosDaPessoa.append(input('Nome: '))
    dadosDaPessoa.append(float(input('Peso: ')))
    if len(pessoasCadastradas) == 0:
        maiorPeso = dadosDaPessoa[1]
        menorPeso = dadosDaPessoa[1]
    else:
        if dadosDaPessoa[1] > maiorPeso:
            maiorPeso = dadosDaPessoa[1]
        if dadosDaPessoa [1] < menorPeso:
            menorPeso = dadosDaPessoa[1]
    pessoasCadastradas.append(dadosDaPessoa[:])
    dadosDaPessoa.clear()
    continuar = str(input('Deseja continuar? [S/N]: ')).lower()
    while continuar not in 'sn':
        continuar = str(input('Dados inválidos. Por favor digite S para continuar e N para parar: '))
    if 'n' in continuar:
        break
print(f'Foram cadastradas {len(pessoasCadastradas)} pessoas')
print(f'O maiorPeso peso digitado foi {maiorPeso}Kg de', end=' ')
for p in pessoasCadastradas:
    if p[1] == maiorPeso:
        print(f'{p[0]}', end=' ')
print(f'\nO menorPeso peso digitado foi {menorPeso}Kg de', end=' ')
for a in pessoasCadastradas:
    if a[1] == menorPeso:
        print(f'{a[0]}', end=' ')