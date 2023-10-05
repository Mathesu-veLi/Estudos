numbers = []

for iterator in range(1, 4):
    numbers.append(int(input(f'Digite o {iterator}° número = ')))
    
print(f'O menor valor digitado é {min(numbers)} e o maior é {max(numbers)}')