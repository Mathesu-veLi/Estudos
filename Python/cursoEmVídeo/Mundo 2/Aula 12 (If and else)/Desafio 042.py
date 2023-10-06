first_straight = float(input('Digite o comprimento da 1° reta: '))
second_straight = float(input('Digite o comprimento da 2° reta: '))
third_straight = float(input('Digite o comprimento da 3° reta: '))

if first_straight < second_straight + third_straight and second_straight < first_straight + third_straight and third_straight < first_straight + second_straight:
    print('As retas acima podem formar um triângulo ', end='')
    if first_straight == second_straight == third_straight:
        print('Equilátero')
    elif first_straight != second_straight != third_straight != first_straight:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Não da para fazer um triângulo com essas retas')
