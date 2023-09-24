número = int(input('Digite um número para saber seu fatorial: '))
multiplicador = 1
passo = número
print(f'{número}! =', end=' ')
while passo > 0:
    print(f'{passo}', end=' ')
    print('.' if passo > 1 else '=', end=' ')
    multiplicador *= passo
    passo -= 1
print(f'{multiplicador}')