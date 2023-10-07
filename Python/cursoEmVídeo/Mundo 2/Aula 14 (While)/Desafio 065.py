average_of_numbers = 0
typed_numbers = []

while True:
    number = int(input('Digite um valor: '))
    average_of_numbers += number
    typed_numbers.append(number)
    
    while True:
        to_continue = str(input('Quer continuar? [S/N]: ')).lower().strip()
        if to_continue in 'ns':
            break
    
    if 'n' in to_continue:
        break

average_of_numbers /= len(typed_numbers)
print(f'O maior número digitado foi {max(typed_numbers)} e o menor foi {min(typed_numbers)}, e a média desses números é {average_of_numbers:.2f}')
