from random import randint


random_number = randint(0, 5)
response = int(input(
    'A maquina pensou em um número de 0 a 5, sabe dizer qual foi esse número? Digite aqui!: '))

if response == random_number:
    print('Parabéns!! Você acertou!')
else:
    print(f'Que pena! Você errou! A resposta era {random_number}')
