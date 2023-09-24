número = int(input('Digite um número: '))
print(f'A tabuada do {número} é:')
for c in range(1, 11):
    print(f'{número} . {c} = {número*c}')
    