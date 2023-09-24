altura = float(input('Qual sua altura?: '))
peso = float(input('Qual seu peso?: '))
imc = peso / (altura ** 2)
print(f'Seu IMC é {imc:.2f}')
if 18.5 > imc:
    print('Você está Abaixo do peso')
elif 18.5 <= imc and imc < 25:
    print('Você está no Peso Ideal')
elif 25 <= imc and imc < 30:
    print('Você está Sobrepeso')
elif 30 <= imc and imc < 40:
    print('Você está em Obesidade')
elif  40 <= imc:
    print('Você está em Obesidade mórbida')