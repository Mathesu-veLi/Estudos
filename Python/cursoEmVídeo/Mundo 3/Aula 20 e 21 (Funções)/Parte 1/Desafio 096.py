from modules import calculate_area

while True:
    try:
        width = float(input('LARGURA (m): '))
        height = float(input('COMPRIMENTO (m): '))
        break
    except ValueError:
        print('Dígite somente números por favor')

print(f'A área de um terreno {width: .2f} x {height: .2f} é de {
      calculate_area(width, height)}m²')
