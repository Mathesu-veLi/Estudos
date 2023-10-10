matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
even = sum_of_third_column_values = sum_of_second_line_values = 0

for x in range(0, 3):
    for y in range(0, 3):
        matrix[x][y] = int(input(f'Digite um valor para [{x}, {y}]: '))

        if matrix[x][y] % 2 == 0:
            even += matrix[x][y]
        if y == 2:
            sum_of_third_column_values += matrix[x][y]
        if x == 1:
            sum_of_second_line_values += matrix[x][y]

for x in range(0, 3):
    for y in range(0, 3):
        print(f'[{matrix[x][y]:^5}]', end='')
    print()

print(f'A soma dos valores pares é {even}')
print(f'A soma dos valores da terceira coluna é {sum_of_third_column_values}')
print(f'O maior valor da segunda linha é {sum_of_second_line_values}')
