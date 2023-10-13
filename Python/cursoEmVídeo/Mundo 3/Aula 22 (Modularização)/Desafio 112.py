from CEVUtils import currency
from CEVUtils.check_if_is_number import check_if_is_number


price = check_if_is_number('Digite o preço: R$',
                           'Digite somente valores monetários por favor!')
currency.show_price_changes(price, 80, 30)
