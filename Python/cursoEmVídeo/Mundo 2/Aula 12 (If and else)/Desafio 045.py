from random import choice


jogadaDoComputador = choice(['Pedra', 'Papel', 'Tesoura'])

user = str(input('Vamos brincar de Jokempô! Escolha pedra, papel ou tesoura e tente me vencer!: ')).strip().capitalize()

print(f"O computador escolheu {jogadaDoComputador}!")
if user == jogadaDoComputador:
    print('Empatou!')
    
elif user == 'Pedra' and jogadaDoComputador == 'Tesoura' or user == 'Papel' and jogadaDoComputador == 'Pedra' or user == 'Tesoura' and jogadaDoComputador == 'Papel':
    print('Você venceu!')

else:
    print('Você perdeu!')