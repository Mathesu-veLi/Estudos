from random import randint
from time import sleep


number_set = []
number_sets = []
quantity_of_number_sets = int(input('Quantos jogos você quer que eu sorteie? '))

for iterator in range(quantity_of_number_sets):
    for second_iterator in range(6):
        random_number = randint(1, 60)
        if random_number not in number_set:
            number_set.append(random_number)

    number_set.sort()
    number_sets.append(number_set[:])
    number_set.clear()
    
for iterator, set in enumerate(number_sets):
    print(f'Jogo {iterator + 1}: {set}')
    sleep(0.5)
print(f'{"<" * 4} Boa sorte! {">" * 4}')