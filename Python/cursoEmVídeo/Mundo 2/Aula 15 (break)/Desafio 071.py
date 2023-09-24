valor = int(input('Qual vai ser o valor sacado?: R$'))
total = valor
cédulas = 50
totalDeCédulas = 0
while True:
    if total >= cédulas:
        total -= cédulas
        totalDeCédulas += 1
    else:
        if totalDeCédulas > 0:
            print(f'Você sacou {totalDeCédulas} cédulas de R${cédulas}')
        if cédulas == 50:
            cédulas = 20
        elif cédulas == 20:
            cédulas = 10
        elif cédulas == 10:
            cédulas = 1
        totalDeCédulas = 0
        if total == 0:
            break