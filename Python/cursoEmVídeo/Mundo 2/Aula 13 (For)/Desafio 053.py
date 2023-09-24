frase = str(input('Digite uma frase para saber se ela é uma frase palíndroma: ')).strip().lower()
print(f'A frase digitada ao contrario é {frase[::-1]}')
print('A frase digitada', end=' ')
if frase[::-1] == frase:
     print('é um palíndromo')
else:
    print('não é um palíndromo')