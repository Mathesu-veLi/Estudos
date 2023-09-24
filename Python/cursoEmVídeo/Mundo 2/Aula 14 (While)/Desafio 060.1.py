número = int(input('Digite um número para saber seu fatorial: '))
multiplicador = 1
print(f'{número}! =', end=' ')
for g in range(número, 0, -1):
    print(f'{g}', end=' ')
    print('x' if g > 1 else '=', end=' ')
    multiplicador *= g
print(f'{multiplicador}')