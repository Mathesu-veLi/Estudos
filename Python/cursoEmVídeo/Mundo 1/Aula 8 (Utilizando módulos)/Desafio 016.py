from math import floor

while True:
    decimalNumber = str(input('Digite um número decimal: '))
    decimalNumber = decimalNumber.replace(',', '.')
    try:
        decimalNumber = float(decimalNumber)
        break
    except:
        print('Digite um valor válido!')
    

print(f'O número {decimalNumber:.2f} tem a parte inteira {floor(decimalNumber)}')