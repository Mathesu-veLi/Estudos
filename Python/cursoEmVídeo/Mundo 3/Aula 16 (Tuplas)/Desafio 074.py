from random import randint


númerosAleatórios = randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)
print("Os valores sorteados foram:", end=' ')
for c in númerosAleatórios:
    print(f'{c}', end=' ')
print(f'\nO maior número randômico foi {max(númerosAleatórios)} e o menor foi {min(númerosAleatórios)}')