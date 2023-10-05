from math import floor

while True:
    decimal_number = str(input('Digite um número decimal: '))
    decimal_number = decimal_number.replace(',', '.')
    try:
        decimal_number = float(decimal_number)
        break
    except:
        print('Digite um valor válido!')


print(
    f'O número {decimal_number:.2f} tem a parte inteira {floor(decimal_number)}')
