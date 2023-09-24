velocidade = int(input('Você está dirigindo um carro. Qual a velocidade dele?: '))
print('O limite de velocidade é 80')
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você ultrapassou o limite de velocidade!\nVocê terá que pagar R${multa:.2f} de multa')
else:
    print('Você não ultrapassou o limite de velocidade')