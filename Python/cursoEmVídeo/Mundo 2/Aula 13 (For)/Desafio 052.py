total_of_divisible_numbers = 0
number = int(input('Digite um número: '))
for iterator in range(1, number + 1):
    if number % iterator == 0:
        total_of_divisible_numbers += 1 

print(
    f'O número {number} foi divisível por {total_of_divisible_numbers} números, logo, ele', end=' ')
if total_of_divisible_numbers != 2:
    print('não é um número primo')
else:
    print('é um número primo')
