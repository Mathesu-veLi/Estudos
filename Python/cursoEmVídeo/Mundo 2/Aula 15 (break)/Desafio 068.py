from random import randint


vitóriasConsecutivas = 0
while True:
    númeroEscolhido = randint(0, 10)
    escolhaDoUsuário = 0
    
    while escolhaDoUsuário != 1 and escolhaDoUsuário != 2:
        escolhaDoUsuário = int(input('Vamos jogar par ou impar!\nDigite 1 para se escolhe impar ou 2 se escolhe par: '))
    
    númeroDigitado = int(input('Agora escolha um número: '))
    númeroFinal = númeroEscolhido + númeroDigitado
    
    print(f'O computador escolheu {númeroEscolhido} e você escolheu {númeroDigitado}, logo, ', end='')
    if escolhaDoUsuário == 2 and númeroFinal % 2 == 0 or escolhaDoUsuário == 1 and númeroFinal % 2 != 0:
        print('você \033[32mVENCEU!\033[m')
        vitóriasConsecutivas += 1
    else:
        print('você \033[31mPERDEU!\033[m')
        break
print(f'Game Over!\nVocê teve {vitóriasConsecutivas} vitórias consecutivas')