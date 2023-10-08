print('Digite 4 números:')
numbers = int(input()), int(input()), int(input()), int(input())
print('Você digitou os números: ', end='')
for number in numbers:
    print(number, end=' ')
print()

if numbers.count(9) > 0:
    print(f'O número 9 aparece {numbers.count(9)} vezes entre os números digitados')
else:
    print('O número 9 não foi digitado')

if numbers.count(3) > 0:
    print(f'O número 3 aparece pela primeira vez na {numbers.index(3) + 1}ª posição')
else:
    print('O número 3 não foi digitado')

print('Os números pares digitados foram: ', end='')
for number in numbers:
    if number % 2 == 0:
        print(number, end=' ')