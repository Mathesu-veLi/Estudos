from random import choice


choice_of_the_computer = choice(['Pedra', 'Papel', 'Tesoura'])

choice_of_the_user = str(input(
    'Vamos brincar de Jokempô! Escolha pedra, papel ou tesoura e tente me vencer!: ')).strip().capitalize()

print(f"O computador escolheu {choice_of_the_computer}!")

if choice_of_the_user == choice_of_the_computer:
    print('Empatou!')

elif choice_of_the_user == 'Pedra' and choice_of_the_computer == 'Tesoura' or choice_of_the_user == 'Papel' and choice_of_the_computer == 'Pedra' or choice_of_the_user == 'Tesoura' and choice_of_the_computer == 'Papel':
    print('Você venceu!')

else:
    print('Você perdeu!')
