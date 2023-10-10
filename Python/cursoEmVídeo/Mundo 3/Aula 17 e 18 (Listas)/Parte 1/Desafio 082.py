numbers = []
while True:
    numbers.append(int(input('Digite um número: ')))
    to_continue = str(input('Deseja continuar? [S/N]: ')).lower()
    while to_continue not in 'sn':
        to_continue = str(
            input('Dados inválidos. Por favor digite S para continuar e N para parar: ')).lower()
    if 'n' in to_continue:
        break

even_numbers = []
odd_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
print(f'Os números digitados foram: {numbers}')
print(f'Os números pares digitados foram: {even_numbers}')
print(f'E os impares foram: {odd_numbers}')
