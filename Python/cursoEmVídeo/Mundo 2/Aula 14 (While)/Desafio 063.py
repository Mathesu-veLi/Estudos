terms = int(input('Quantos termos você quer mostrar?: '))
counter = last_number = 0
penultimate_number = 1

while counter != terms:
    number = last_number
    print(f'{number} -> ', end='')
    
    last_number = penultimate_number + number
    penultimate_number = number
    counter += 1
print('FIM')