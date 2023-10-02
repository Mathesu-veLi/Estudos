from random import choice


choiceOfTheComputer = choice(['Pedra', 'Papel', 'Tesoura'])

choiceOfTheUser = str(input('Vamos brincar de Jokempô! Escolha pedra, papel ou tesoura e tente me vencer!: ')).strip().capitalize()

print(f"O computador escolheu {choiceOfTheComputer}!")

if choiceOfTheUser == choiceOfTheComputer:
    print('Empatou!')
    
elif choiceOfTheUser == 'Pedra' and choiceOfTheComputer == 'Tesoura' or choiceOfTheUser == 'Papel' and choiceOfTheComputer == 'Pedra' or choiceOfTheUser == 'Tesoura' and choiceOfTheComputer == 'Papel':
    print('Você venceu!')

else:
    print('Você perdeu!')