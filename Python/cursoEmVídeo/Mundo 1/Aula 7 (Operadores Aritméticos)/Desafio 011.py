wall = {
    'width': float(input('Digite aqui qual a largura da sua parede: ')),
    'height': float(input('Agora digite a altura: ')),
}

wall['area'] = float(wall['width'] * wall['height'])
wall['amount_of_paint_to_paint'] = float(wall['area'] / 2)

print(f'Sua parede tem {wall["area"]:.2f}m² de área')
print(
    f'Precisaria de {wall["amount_of_paint_to_paint"]:.2f}l de tinta para pinta-la')
