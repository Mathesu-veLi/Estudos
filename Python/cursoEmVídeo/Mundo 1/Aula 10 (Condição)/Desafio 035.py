firstStraight = float(input('Digite o comprimento da 1° reta: '))
secondStraight = float(input('Digite o comprimento da 2° reta: '))
thirdStraight = float(input('Digite o comprimento da 3° reta: '))

if firstStraight < secondStraight + thirdStraight and secondStraight < firstStraight + thirdStraight and thirdStraight < firstStraight + secondStraight:
    print('É possível fazer um triângulo com essas retas')
else:
    print('Não é possível fazer um triângulo com essas retas')