totalDeNúmerosDivisíveis = 0
número = int(input('Digite um número: '))
for c in range(1, número + 1):
    if número % c == 0:
        totalDeNúmerosDivisíveis += 1
print(f'O número {número} foi divisível por {totalDeNúmerosDivisíveis} números, logo, ele', end=' ')
if totalDeNúmerosDivisíveis == 2:
    print('é um número primo')
else:
    print('não é um número primo')