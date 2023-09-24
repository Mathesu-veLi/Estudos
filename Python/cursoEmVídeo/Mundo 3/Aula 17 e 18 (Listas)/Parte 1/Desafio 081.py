valores = []
while True:
    valores.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar? [S/N]: ')).lower()
    while continuar not in 'sn':
        continuar = str(input('Dados inválidos. Por favor digite S para continuar e N para parar: '))
    if 'n' in continuar:
        break
valores.sort(reverse=True)
print(f"Foram digitados {len(valores)} valores, são eles:\n{valores}\nE o valor 5", end=' ')
if 5 in valores:
    print('foi digitado')
else:
    print('não foi digitado')
