while True:
    gender = str(input('Informe seu sexo [M/F]: ')).strip().lower()[0]
    if 'm' in gender or 'f' in gender:
        print(f'Sexo {gender} registrado com sucesso')
        break
    gender = str(
        input('Dados inválidos. Digite seu sexo novamente [M/F]: ')).strip().lower()[0]
