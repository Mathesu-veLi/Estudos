firstNumber = int(input('Digite um número: '))
secondNumber = int(input('Digite outro número: '))

if firstNumber > secondNumber:
    print(f'O número {firstNumber} é o maior valor')
elif firstNumber < secondNumber:
    print(f'O número {secondNumber} é o maior valor')
else:
    print('Os dois valores são iguais')
