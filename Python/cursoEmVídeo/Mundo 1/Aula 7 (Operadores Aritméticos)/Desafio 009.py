número = int(input('Digite um número para ver sua tabuada: '))
print(f'A tabuada de {número} é:')
for c in range(1, 11):
    print(f'{número} . {c} = {número * c}')