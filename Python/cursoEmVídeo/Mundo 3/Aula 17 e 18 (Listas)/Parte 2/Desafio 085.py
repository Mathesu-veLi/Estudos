values = [[], []]

for iterator in range(0, 7):
    value = int(input('Digite um número: '))
    if value % 2 == 0:
        values[0].append(value)
    else:
        values[1].append(value)
        
values[0].sort()
values[1].sort()

print(f'Os valores pares digitados foram: {values[0]}')
print(f'Os valores impares digitados foram: {values[1]}')