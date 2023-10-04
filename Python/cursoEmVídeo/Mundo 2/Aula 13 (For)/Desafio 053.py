text = str(input('Digite uma frase para saber se ela é uma frase palíndroma (sem acentos): ')).strip().lower().replace(' ', '')
for char in ".!?,-":
        text = text.replace(char, "")

print(f'A frase digitada ao contrario é {text[::-1]}')
print('A frase digitada', end=' ')

text[::-1] != text and print('não', end=' ')
print('é um palíndromo')