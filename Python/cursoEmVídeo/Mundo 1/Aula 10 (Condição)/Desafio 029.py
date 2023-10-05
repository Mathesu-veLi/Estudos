car_speed = int(input('Você está dirigindo um carro. Qual a velocidade dele?: '))
print('O limite de velocidade é 80')

if car_speed > 80:
    penalty = (car_speed - 80) * 7
    print(f'Você ultrapassou o limite de velocidade!\nVocê terá que pagar R${penalty:.2f} de multa')
else:
    print('Você não ultrapassou o limite de velocidade')