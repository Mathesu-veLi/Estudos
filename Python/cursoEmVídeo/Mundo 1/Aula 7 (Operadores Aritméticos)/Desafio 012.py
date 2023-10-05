price = float(
    input('Digamos que você tenha um produto, qual o preço ele teria?: R$'))
price_with_disconot = price - (price * 0.05)
print(
    f'Se você me desse 5% de desconto nesse produto, iria vende-lo a mim por R${price_with_disconot:.2f}')
