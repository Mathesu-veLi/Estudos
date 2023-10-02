widthOfWall = float(input('Digite aqui qual a largura da sua parede: '))
heightOfWall = float(input('Agora digite a altura: '))
areaOfWall = widthOfWall * heightOfWall
amountOfInkNeededToPaintTheWall = areaOfWall / 2
print(f'Sua parede tem {areaOfWall:.2f}m² de área')
print(f'Precisaria de {amountOfInkNeededToPaintTheWall:.2f}l de tinta para pinta-la')