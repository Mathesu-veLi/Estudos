número = int(input('Digite um número inteiro: '))
base = int(input('''Se quiser converter esse número em:
                 Binário:  Digite 1
                 Octal:  Digite 2
                 Hexadecimal:  Digite 3
                 Escolha: '''))
if base == 1:
    bin = bin(número)
    print(f'{número} em binário é {bin[2:]}')
elif base == 2:
    octal = oct(número)
    print(f'{número} em octal é {octal[2:]}')
elif base == 3:
    hexa = hex(número)
    print(f'{número} em hexadecimal é {hexa[2:]}')