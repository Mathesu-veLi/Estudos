ordem = 1
mulheresAbaixoDe20Anos = pessoasComMaisDe18Anos = homensCadastrados = pessoasCastradas = 0
while True:    
    idade = int(input(f'Digite a idade da {ordem}° pessoa: '))
    ordem += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite agora o sexo dela [M/F]: ')).upper()
    if idade < 20 and sexo == 'F':
        mulheresAbaixoDe20Anos += 1
    if sexo == 'M':
        homensCadastrados += 1
    if idade >= 18:
        pessoasComMaisDe18Anos += 1
    pessoasCastradas += 1
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Deseja cadastrar mais alguma pessoa? [S/N]: ')).lower()
    if 'n' in continuar:
        break
print(f'''Foram cadastradas {pessoasCastradas} pessoas
      {pessoasComMaisDe18Anos} tem mais de 18 anos
      {mulheresAbaixoDe20Anos} são mulheres abaixo dos 20 anos
      {homensCadastrados} são homens''')