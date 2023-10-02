firstStraight = float(input('Digite o comprimento da 1° reta: '))
secondStraight = float(input('Digite o comprimento da 2° reta: '))
thirdStraight = float(input('Digite o comprimento da 3° reta: '))

if firstStraight < secondStraight + thirdStraight and secondStraight < firstStraight + thirdStraight and thirdStraight < firstStraight + secondStraight:
    print('As retas acima podem formar um triângulo ', end='')
    if firstStraight == secondStraight == thirdStraight:
        print('Equilátero')
    elif firstStraight != secondStraight != thirdStraight != firstStraight:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Não da para fazer um triângulo com essas retas')