print('Digite 4 números:')
números = int(input()), int(input()), int(input()), int(input())
print('Você digitou os números: ', end='')
for n in números:
    print(n, end=' ')
print()
if números.count(9) > 0:
    print(f'O número 9 aparece {números.count(9)} vezes entre os números digitados')
else:
    print('O número 9 não foi digitado')
if números.count(3) > 0:
    print(f'O número 3 aparece pela primeira vez na {números.index(3) + 1}ª posição')
else:
    print('O número 3 não foi digitado')
print('Os números pares digitados foram: ', end='')
for c in números:
    if c % 2 == 0:
        print(c, end=' ')