sum = 0
quantity_of_values = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        quantity_of_values += 1
        sum += c

print(
    f'A soma dos {quantity_of_values} valores múltiplos de 3 de 0 a 500 é {sum}')
