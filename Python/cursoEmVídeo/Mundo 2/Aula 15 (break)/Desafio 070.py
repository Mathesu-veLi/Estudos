final_price = cheapest_product_price = products_over_a_thousand_reais = 0
cheapest_product_name = ''

while True:
    product = {
        'product_name': str(input('Digite o nome do produto: ')),
        'product_price': float(input('Digite o preço dele: R$'))
    }
    final_price += product['product_price']
    
    if final_price == product['product_price']:
        cheapest_price = cheapest_product_price = product['product_price']
        cheapest_product_name = product['product_name']
        
    if product['product_price'] > 1000:
        products_over_a_thousand_reais += 1
        
    if product['product_price'] < cheapest_price:
        cheapest_product_name = product['product_name']
        cheapest_product_price = product['product_price']
        
    while True:
        to_continue = str(input('Deseja continuar? [S/N]: ')).lower()
    
        if to_continue in 'ns':
            break
        else:
            print('Digite S para cadastrar mais produtos e N caso não quiser')

    if 'n' in to_continue:
        break
    
print(f'O total gasto na compra foi de R${final_price:.2f}')

if products_over_a_thousand_reais != 0:
    print(f'{products_over_a_thousand_reais} produtos custam mais de R$1000')

print(f'E o(a) {cheapest_product_name} é o produto mais barato, custando apenas R${cheapest_product_price:.2f}')
