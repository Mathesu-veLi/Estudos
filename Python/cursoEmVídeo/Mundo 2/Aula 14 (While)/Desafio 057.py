sexo = str(input('Informe seu sexo [M/F]: ')).strip().lower()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Digite seu sexo novamente [M/F]: ')).strip().lower()[0]
print(f'Sexo {sexo} registrado com sucesso')