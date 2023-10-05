first_straight = float(input('Digite o comprimento da 1° reta: '))
second_straight = float(input('Digite o comprimento da 2° reta: '))
third_straight = float(input('Digite o comprimento da 3° reta: '))

if first_straight < second_straight + third_straight and second_straight < first_straight + third_straight and third_straight < first_straight + second_straight:
    print('É possível fazer um triângulo com essas retas')
else:
    print('Não é possível fazer um triângulo com essas retas')
