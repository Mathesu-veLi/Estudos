expression = str(input(
    'Digite uma expressão numérica que use parênteses e eu verei se ele está fechado na ordem correta!: '))

quantity_of_parentheses = []
for char in expression:
    if char in '()':
        quantity_of_parentheses.append(char)

if len(quantity_of_parentheses) % 2 == 0:
    print('A expressão é válida')
else:
    print('A expressão é inválida!')
