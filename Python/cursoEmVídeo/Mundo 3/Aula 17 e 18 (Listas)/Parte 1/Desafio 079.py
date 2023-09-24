valores = []
while True:
    valor = int(input('Digite um número: '))
    if valor in valores:
        print('Digite um número que não tenha digitado antes')
        continue
    else:
        valores.append(valor)
    continuar = input('Deseja continuar? [S/N]: ').lower()
    while continuar not in 'sn':
        continuar = str(input('Dados inválidos. Por favor digite S para continuar e N para parar: '))
    if continuar in 'n': 
        break
valores.sort()
print(f'Os valores únicos digitados foram: {valores}')