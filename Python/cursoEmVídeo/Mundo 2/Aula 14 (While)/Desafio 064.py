sum = quantity_of_numbers = 0
number = int(input('Digite um número (Digite 999 para sair do programa): '))

while number != 999:
    sum += number
    quantity_of_numbers += 1
    number = int(input('Digite outro número: '))

print(
    f'Foram digitados {quantity_of_numbers} números e a soma desses valores é {sum}')
