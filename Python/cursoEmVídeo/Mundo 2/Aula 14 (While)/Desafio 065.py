continuation_confirmation = 's'
average_of_numbers = 0
typed_numbers = []

while True:
    number = int(input('Digite um valor: '))
    average_of_numbers += number
    typed_numbers.append(number)
    
    while True:
        continuation_confirmation = str(input('Quer continuar? [S/N]: ')).lower().strip()
        if 's' in continuation_confirmation or 'n' in continuation_confirmation:
            break
    
    if 'n' in continuation_confirmation:
        break

average_of_numbers /= len(typed_numbers)
print(f'O maior número digitado foi {max(typed_numbers)} e o menor foi {min(typed_numbers)}, e a média desses números é {average_of_numbers:.2f}')
