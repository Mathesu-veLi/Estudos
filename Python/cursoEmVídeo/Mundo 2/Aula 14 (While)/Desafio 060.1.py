number = int(input('Digite um número para saber seu fatorial: '))
multiplier = 1
print(f'{number}! =', end=' ')

for decreased_number in range(number, 0, -1):
    print(decreased_number, end=' ')
    print('.' if decreased_number > 1 else '=', end=' ')

    multiplier *= decreased_number

print(f'{multiplier}')
