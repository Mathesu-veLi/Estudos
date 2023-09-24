números = []
for c in range(1, 4):
    números.append(int(input(f'Digite o {c}° numero = ')))
print(f'O menor valor digitado é {min(números)} e o maior é {max(números)}')