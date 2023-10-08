values = list()

for value in range(0, 5):
    values.append(int(input('Digite um valor: ')))

print(f'Os valores digitados foram:\n{values}')
print(f'O maior valor digitado foi {max(values)} na {values.index(max(values))}° posição e o menor foi {min(values)} na {values.index(min(values))}° posição')