number = int(input('Digite um número: '))

print(f'A tabuada do {number} é:')
for multiplier in range(1, 11):
    print(f'{number} . {multiplier} = {number*multiplier}')
    