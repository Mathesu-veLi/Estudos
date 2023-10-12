def read_number(ask, error_mensage='Digite somente números por favor!', type=int):
    """-> Allows input of numbers only

    Args:
        ask (str): Message that will appear in the input
        error_mensage (str, optional): Error message that will appear if the value entered is not a number. Defaults to 'Digite somente números por favor!'.
        type (str, optional): Type of number to be entered (int ou float)
    """

    while True:
        number = str(input(ask)).strip()
        try:
            if type == int:
                number = int(number)
            elif type == float:
                if ',' in number:
                    number = number.replace(',', '.')
                number = float(number)
            return number
        except ValueError:
            print(error_mensage)