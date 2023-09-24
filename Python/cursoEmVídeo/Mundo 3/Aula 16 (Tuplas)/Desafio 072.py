números = 'zero', 'um', 'dois', 'trés', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    número = int(input('Digite um número de 0 a 20 para ver ele em extenso: '))
    if número > 20:
        print('Tente novamente. ', end='')
    print(f'{número} em extenso é {números[número]}')
