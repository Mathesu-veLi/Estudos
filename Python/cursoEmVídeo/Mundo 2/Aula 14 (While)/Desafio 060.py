number = int(input('Digite um número para saber seu fatorial: '))
multiplier = 1
decreased_number = number
print(f'{number}! =', end=' ')

while decreased_number > 0:
    print(decreased_number, end=' ')
    print('.' if decreased_number > 1 else '=', end=' ')

    multiplier *= decreased_number
    decreased_number -= 1

print(multiplier)
