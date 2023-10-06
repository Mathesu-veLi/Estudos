from random import randint


chosen_number = randint(0, 10)
attempts = 1
typed_number = int(
    input('O computador pensou em um número! Tente acertar qual foi!: '))

while typed_number != chosen_number:
    if typed_number > chosen_number:
        typed_number = int(input('Um pouco menos... Tente novamente: '))
    else:
        typed_number = int(input('Um pouco mais... Tente novamente: '))

    attempts += 1

print(f'Você acertou depois de {attempts} tentativas. Parabéns!')
