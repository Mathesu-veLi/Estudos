numbers = 'zero', 'um', 'dois', 'trés', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

while True:
    chosen_number = int(input('Digite um número de 0 a 20 para ver ele em extenso [999 para parar]: '))
    if chosen_number <= 20 and chosen_number >= 0:
        break
    print('Tente novamente. ', end='')
    
print(f'{chosen_number} em extenso é {numbers[chosen_number]}')
    
