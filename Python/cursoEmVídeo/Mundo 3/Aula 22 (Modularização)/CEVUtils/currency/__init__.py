def format_to_price_format(price, currency='R$'):
    """returns price formatted with currency

    Args:
        price (float): price to be formatted
        currency (str, optional): currency that the price will be formatted. Defaults to 'R$'.

    Returns:
        str: price formatted with currency
    """

    formatted_price = '\033[32m' + \
        f'{currency}{price: .2f}'.replace('.', ',') + '\033[m'
    return formatted_price


def increase_price_ten_percent(price: float, percentage: float, format=True):
    """increase the price by a custom percentage

    Args:
        price (float): price to be increased
        percentage (float): percentage that the number will be increased
        format (bool, optional): format to currency format. Defaults to True.

    Returns:
        float: increased price
    """

    increased_price = ((price / 100) * percentage) + price

    if format:
        increased_price = format_to_price_format(increased_price)
    return increased_price


def reduce_price_ten_percent(price, percentage, format=True):
    """reduce the price by a custom percentage

    Args:
        price (float): price to be reduced
        percentage (float): percentage that the number will be reduced
        format (bool, optional): format to currency format. Defaults to True.

    Returns:
        float: increased price
    """

    reduced_price = price - ((price / 100) * percentage)

    if format:
        reduced_price = format_to_price_format(reduced_price)
    return reduced_price


def double_price(price, format=True):
    """double the price 

    Args:
        price (float): price to be doubled
        format (bool, optional): format to currency format. Defaults to True.

    Returns:
        float: doubled price
    """

    doubled_price = price * 2

    if format:
        doubled_price = format_to_price_format(doubled_price)
    return doubled_price


def halve_the_price(price, format=True):
    """divide the price in half

    Args:
        price (float): price to be helved
        format (bool, optional): format to currency format. Defaults to True.

    Returns:
        float: helved price
    """

    price_halved = price / 2

    if format:
        price_halved = format_to_price_format(price_halved)
    return price_halved


def show_price_changes(price, increase_percentage, reduction_percentage):
    print('-' * 30)
    print('Resumo de valores'.center(30))
    print('-' * 30)

    print(f'Preço analizado: {f"{format_to_price_format(price)}": >22}')
    print(f'Dobro do preço: {f"{double_price(price, True)}": >23}')
    print(f'Metade do preço: {f"{halve_the_price(price, True)}": >22}')

    print(f'{increase_percentage}% de aumento: {
          f"{increase_price_ten_percent(price, increase_percentage, True)}": >23}')
    print(f'{reduction_percentage}% de redução: {
          f"{reduce_price_ten_percent(price, reduction_percentage, True)}": >23}')
    print('-' * 30)
