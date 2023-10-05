while True:
    distance = str(input('Digite a distancia da viagem: ')).lower()

    if 'km' in distance:
        distance = distance.replace('km', '')
    try:
        distance = float(distance)
        if distance < 200:
            ticket = distance * 0.50
            print(f'O preço da passagem será R${ticket:.2f}')
        else:
            ticket = distance * 0.45
            print(f'O preço da passagem será R${ticket:.2f}')
        break
    except:
        print('Digite um valor válido (ex: 40)')
