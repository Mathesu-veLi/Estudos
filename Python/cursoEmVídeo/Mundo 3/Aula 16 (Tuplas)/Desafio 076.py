products = ('Pão', 0.25, 'Pc Gamer', 11000, 'Monitor Razer', 2000, 'Mouse Razer', 500, 'Galaxy Core Prime', 2000)

for position in range(0, len(products)):
    if position % 2 == 0:
        print(f'{products[position]:.<30}', end='')
    else:
        print(f'R${products[position]:>8.2f}')