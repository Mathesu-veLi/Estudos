from modules import calculate_factorial


number = int(input('Digite um número para ver seu fatorial: '))
print(f'O fatorial de {number} é {calculate_factorial(number, True)}')
