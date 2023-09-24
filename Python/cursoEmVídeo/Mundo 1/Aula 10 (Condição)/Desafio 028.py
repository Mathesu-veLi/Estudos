from random import randint
número = randint(0, 5)
resposta = int(input('A maquina pensou em um número de 0 a 5, sabe dizer qual foi esse número? Digite aqui!: '))
if resposta == número:
    print('Parabéns!! Você acertou!')
else:
    print(f'Que pena! Você errou! A resposta era {número}')
