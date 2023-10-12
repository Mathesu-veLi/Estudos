from CEVUtils import currency
from CEVUtils.read_number import read_number


price = read_number('Digite o preço: R$',
                    'Digite somente valores monetários por favor!')
currency.show_price_changes(price, 80, 30)
