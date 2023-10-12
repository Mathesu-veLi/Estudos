from CEVUtils import currency

price = float(input('Digite o preço: R$'))
formatted_price = currency.format_to_price_format(price)

print(f'A metade de {formatted_price} é {
      currency.halve_the_price(price)}')
print(f'O dobro de {formatted_price} é {currency.double_price(price)}')

print(f'Aumentando 10%, temos {
      currency.increase_price_ten_percent(price, 10)}')
print(f'Reduzindo 13%, temos {currency.reduce_price_ten_percent(price, 13)}')
