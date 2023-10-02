number = int(input('Digite um número para ver sua tabuada: '))
print(f'A tabuada de {number} é:')
for multiplier in range(1, 11):
    print(f'{number} . {multiplier} = {number * multiplier}')