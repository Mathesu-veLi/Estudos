height = float(input('Qual sua altura?: '))
weight = float(input('Qual seu peso?: '))
bodyMassIndex = weight / (height ** 2)

print(f'Seu IMC é {bodyMassIndex:.2f}')

print('Você está ', end='')
if 18.5 > bodyMassIndex:
    print('Abaixo do peso')
elif 18.5 <= bodyMassIndex and bodyMassIndex < 25:
    print('no Peso Ideal')
elif 25 <= bodyMassIndex and bodyMassIndex < 30:
    print('Sobrepeso')
elif 30 <= bodyMassIndex and bodyMassIndex < 40:
    print('em Obesidade')
elif  40 <= bodyMassIndex:
    print('em Obesidade mórbida')