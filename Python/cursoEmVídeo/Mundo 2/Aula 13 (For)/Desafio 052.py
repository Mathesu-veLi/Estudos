totalOfDivisibleNumbers = 0
number = int(input('Digite um número: '))
for c in range(1, number + 1):
    totalOfDivisibleNumbers += 1 if number % c == 0 else None

print(f'O número {number} foi divisível por {totalOfDivisibleNumbers} números, logo, ele', end=' ')
totalOfDivisibleNumbers != 2 and print('não', end=' ')
print('é um número primo')