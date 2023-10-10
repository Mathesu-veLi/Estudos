matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for x in range(0, 3):
    for y in range(0, 3):
        matrix[x][y] = int(input(f'Digite um valor para [{x}, {y}]: '))

for x in range(0, 3):
    for y in range(0, 3):
        print(f'[{matrix[x][y]:^5}]', end='')
    print()
