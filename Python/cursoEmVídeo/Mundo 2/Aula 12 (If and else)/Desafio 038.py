primeiroNúmero = int(input('Digite um número: '))
segundoNúmero = int(input('Digite outro número: '))

if primeiroNúmero > segundoNúmero:
    print(f'O número {primeiroNúmero} é o maior valor')
elif primeiroNúmero < segundoNúmero:
    print(f'O número {segundoNúmero} é o maior valor')
else:
    print('Os dois valores são iguais')
