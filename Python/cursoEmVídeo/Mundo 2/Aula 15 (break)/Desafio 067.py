while True:
    números = int(input('Quer ver a tabuada de que valor? (0 para parar): '))
    if números <= 0:
        break
    for c in range(1, 11):
        print(f'{números} . {c} = {números * c}')
print('Programa finalizado')