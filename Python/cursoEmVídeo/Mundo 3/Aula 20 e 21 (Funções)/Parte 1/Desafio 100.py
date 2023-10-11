from modules import generate_random_numbers, add_up_the_even_numbers

random_numbers = []

generate_random_numbers(random_numbers)
print(f'Os números sorteados foram {random_numbers}')
print(f'A soma entre todos os números pares entre {
      random_numbers} tem o resultado de {add_up_the_even_numbers(random_numbers)}')
