values = []

while True:
    value = int(input('Digite um número: '))
    if value in values:
        print('Digite um número que não tenha digitado antes')
    else:
        values.append(value)
    
        to_continue = str(input('Deseja continuar? [S/N]: ').lower())
        while to_continue not in 'sn':
            to_continue = str(
                input('Dados inválidos. Por favor digite S para continuar e N para parar: '))
    
        if to_continue in 'n':
            break

values.sort()
print(f'Os valores únicos digitados foram: {values}')
