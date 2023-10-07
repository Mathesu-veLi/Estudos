from random import randint


consecutive_wins = 0
while True:
    chosen_number = randint(0, 10)
    user_choice = 0

    while user_choice != 1 and user_choice != 2:
        print('Vamos jogar par ou impar!')
        user_choice = int(
            input('Digite 1 para se escolhe impar ou 2 se escolhe par: '))

    typed_number = int(input('Agora escolha um número: '))
    result = chosen_number + typed_number

    print(
        f'O computador escolheu {chosen_number} e você escolheu {typed_number}, logo, ', end='')
    if user_choice == 2 and result % 2 == 0 or user_choice == 1 and result % 2 != 0:
        print('você \033[32mVENCEU!\033[m')
        consecutive_wins += 1
    else:
        print('você \033[31mPERDEU!\033[m')
        break

print(f'Game Over!\nVocê teve {consecutive_wins} vitórias consecutivas')
