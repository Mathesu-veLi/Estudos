words = ('galo', 'pássaro', 'azul', 'code')

for word in words:
    print(f'\nNa palavra {word.upper()} temos', end=' ')
    for letter in word:
        if letter.lower() in 'aeiou':
            print(letter, end=' ')