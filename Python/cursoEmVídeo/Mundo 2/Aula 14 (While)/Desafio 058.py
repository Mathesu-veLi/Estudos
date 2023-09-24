from random import randint


númeroEscolhido = randint(0, 10)
tentativas = 1
númeroDigitado = int(input('O computador pensou em um número! Tente acertar qual foi!: '))

while númeroDigitado != númeroEscolhido:
    if númeroDigitado > númeroEscolhido:
        númeroDigitado = int(input('Um pouco menos... Tente novamente: '))
    else:
        númeroDigitado = int(input('Um pouco mais... Tente novamente: '))
        
    tentativas += 1

print(f'Você acertou depois de {tentativas} tentativas. Parabéns!')