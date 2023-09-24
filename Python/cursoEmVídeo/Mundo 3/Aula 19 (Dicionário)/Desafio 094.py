pessoasCadastradas = []
média = []
nomesDasMulheresCadastradas = []
nomeDasPessoasComIdadeAcimaDaMédia = []

while True:
    informaçõesPessoais = {'nome': input('Qual o nome?: '),
            'sexo': input('Qual o sexo? [M/F]: '),
            'idade': int(input('Qual a idade?: '))}
    pessoasCadastradas.append(informaçõesPessoais.copy())
    informaçõesPessoais.clear()
    continuar = str(input('Deseja continuar? [S/N]: ')).lower()
    while continuar not in 'sn':
        continuar = str(input('Dados inválidos. Por favor digite S para continuar e N para parar: '))
    if 'n' in continuar:
        break
print(f'Foram cadastradas {len(pessoasCadastradas)} pessoas')
for c in pessoasCadastradas:
    for k, v in c.items():
        if k == 'idade':
            média.append(v)
        if k == 'sexo':
            if v == 'F':
                for a, b in c.items():
                    if a == 'nome':
                        nomesDasMulheresCadastradas.append(b)
médiaDasIdades = sum(média) / len(média)
for g in pessoasCadastradas:
    for n, m in g.items():
        if n == 'idade':
            if m > médiaDasIdades:
                nomeDasPessoasComIdadeAcimaDaMédia.append(g.copy())
print(f'A média da idade das pessoas cadastradas é de {médiaDasIdades}\nO nome das mulheres cadastradas é:')
for l in nomesDasMulheresCadastradas:
    print(f'    {l}')
print('O nome das pessoas com idade acima da média é:')
for q in nomeDasPessoasComIdadeAcimaDaMédia:
    print(f'    {q}')