números = []
while True:
    números.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar? [S/N]: ')).lower()
    while continuar not in 'sn':
        continuar = str(input('Dados inválidos. Por favor digite S para continuar e N para parar: '))
    if 'n' in continuar:
        break
númerosPares = []
númerosImpares = []
for c in números:
    if c % 2 == 0:
        númerosPares.append(c)
    else:
        númerosImpares.append(c)
print(f'Os números digitados foram:\n{números}\nOs números pares digitados foram:\n{númerosPares}\nE os impares foram:\n{númerosImpares}')