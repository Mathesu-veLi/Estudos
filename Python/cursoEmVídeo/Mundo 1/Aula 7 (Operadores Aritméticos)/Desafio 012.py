preço = float(input('Digamos que você tenha um produto, qual o preço ele teria?: R$'))
preçoComDesconto = preço - (preço * 0.05)
print(f'Se você me desse 5% de desconto nesse produto, iria vende-lo a mim por R${preçoComDesconto:.2f}')