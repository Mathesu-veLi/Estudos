values = []

while True:
    values.append(int(input('Digite um número: ')))
    to_continue = str(input('Deseja continuar? [S/N]: ')).lower()
    while to_continue not in 'sn':
        to_continue = str(input('Dados inválidos. Por favor digite S para continuar e N para parar: '))
    if 'n' in to_continue:
        break

values.sort(reverse=True)

print(f"Foram digitados {len(values)} valores, são eles:\n{values}\nE o valor 5", end=' ')
if 5 in values:
    print('foi digitado')
else:
    print('não foi digitado')
