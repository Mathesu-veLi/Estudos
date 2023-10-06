pair_numbers = 0

for iterator in range(1, 7):
    number = int(input(f'Digite o {iterator}° número: '))
    if number % 2 == 0:
        pair_numbers += number
print(
    f'Se somar-mos só os números pares que você digitou, teriamos o número {pair_numbers}')
