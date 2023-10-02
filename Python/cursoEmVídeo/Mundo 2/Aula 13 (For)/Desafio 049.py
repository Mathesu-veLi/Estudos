number = int(input('Digite um número: '))

print(f'A tabuada do {number} é:')
for c in range(1, 11):
    print(f'{number} . {c} = {number*c}')
    