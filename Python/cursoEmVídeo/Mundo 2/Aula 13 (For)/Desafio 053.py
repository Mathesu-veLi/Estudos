text = str(input('Digite uma frase para saber se ela é uma frase palíndroma (sem acentos): ')).strip().lower()
for char in ".!?,- ":
        text = text.replace(char, "")

print(f'A frase digitada ao contrario é {text[::-1]}')
print('A frase digitada', end=' ')

if text[::-1] != text: 
        print('não é um palíndromo')
else:
        print('é um palíndromo')