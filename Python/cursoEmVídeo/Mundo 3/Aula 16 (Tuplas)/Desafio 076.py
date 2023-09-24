produtos = ('Pão', 0.25, 'Pc Gamer', 11000, 'Monitor Razer', 2000, 'Mouse Razer', 500, 'Galaxy Core Prime', 2000)
for posição in range(0, len(produtos)):
    if posição % 2 == 0:
        print(f'{produtos[posição]:.<30}', end='')
    else:
        print(f'R${produtos[posição]:>8.2f}')