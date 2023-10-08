from random import randint


random_numbers = randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)

print("Os valores sorteados foram:", end=' ')
for number in random_numbers:
    print(f'{number}', end=' ')

print(f'\nO maior número randômico foi {max(random_numbers)} e o menor foi {min(random_numbers)}')