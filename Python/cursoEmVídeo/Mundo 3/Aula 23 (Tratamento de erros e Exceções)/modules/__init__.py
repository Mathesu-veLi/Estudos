def check_if_is_number(ask, error_mensage='Digite somente números por favor!', type=int):
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


def confirm_if_it_will_continue(ask):
    """returns whether or not the user will continue

    Args:
        ask (str): question to continue

    Returns:
        bool: returns True if it continues and False if it doesn't
    """

    while True:
        to_continue = input(f'{ask} [S/N]: ').lower()
        if to_continue not in 'sn':
            print('Erro! Digite S para continuar e N para parar')
        else:
            if 'n' in to_continue:
                return False
            else:
                return True

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


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.register_person()

    def register_person(self):
        """register person in txt file
        """
        registration_file = open("registers.txt", "a", encoding='utf-8')
        registration_file.write(f'\n{(self.name).ljust(35)}{str(f'{self.age} anos').rjust(11)}')


def verify_choice(inputs, limit, errormsg):
    """checks if the number is within the limit

    Args:
        inputs (str): Question that will be asked
        limit (int): number range limit
        errormsg (_type_): error message if number exceeds limit

    Returns:
        int: number
    """

    while True:
        number = check_if_is_number(inputs)
        if number > limit:
            print(errormsg)
        else:
            return number


def decorate_string(string):
    spacing = len(string) + 5
    print('-' * spacing)
    print(f"{string}".center(spacing))
    print('-' * spacing)
