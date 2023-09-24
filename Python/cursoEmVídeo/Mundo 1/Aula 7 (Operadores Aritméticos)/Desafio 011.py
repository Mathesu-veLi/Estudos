largura = float(input('Digite aqui qual a largura da sua parede: '))
altura = float(input('Agora digite a altura: '))
área = largura * altura
tinta = área / 2
print(f'Sua parede tem {área:.2f}m² de área\nPrecisaria de {tinta:.2f}l de tinta para pinta-la')