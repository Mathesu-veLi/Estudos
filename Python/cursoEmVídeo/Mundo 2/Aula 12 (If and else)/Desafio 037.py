number = int(input('Digite um número inteiro: '))
convertTo = int(input('''Se quiser converter esse número em:
                 Binário:  Digite 1
                 Octal:  Digite 2
                 Hexadecimal:  Digite 3
                 Escolha: '''))
if convertTo == 1:
    bin = bin(number)
    print(f'{number} em binário é {bin[2:]}')
elif convertTo == 2:
    octal = oct(number)
    print(f'{number} em octal é {octal[2:]}')
elif convertTo == 3:
    hexa = hex(number)
    print(f'{number} em hexadecimal é {hexa[2:]}')