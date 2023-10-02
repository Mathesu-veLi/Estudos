realMaintenedInTheMoment = float(input('Quantos reais você tem na carteira esse exato momento?: R$'))
realToDollar = realMaintenedInTheMoment / 5.04
print(f'Podes trocar R${realMaintenedInTheMoment:.2f} por US${realToDollar:.2f}')