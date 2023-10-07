while True:
    numbers = int(input('Quer ver a tabuada de que valor? (0 para parar): '))
    
    if numbers <= 0:
        break
    
    for multiplier in range(1, 11):
        print(f'{numbers} . {multiplier} = {numbers * multiplier}')

print('Programa finalizado')
