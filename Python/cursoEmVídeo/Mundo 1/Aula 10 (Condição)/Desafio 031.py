distance = str(input('Digite a distancia da viagem: ')).lower()

if 'km' in distance:
    distance = distance.replace('km', '')
distance = float(distance)

if distance < 200:
    passagem = distance * 0.50
    print(f'O preço da passagem será R${passagem:.2f}')
else:
    passagem = distance * 0.45
    print(f'O preço da passagem será R${passagem:.2f}')