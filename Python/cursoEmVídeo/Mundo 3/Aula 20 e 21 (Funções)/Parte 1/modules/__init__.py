from time import sleep
from random import randint


def write_with_decoration(message: str):
    """Print phrase with '~' embellishment

    Args:
        message (string): Message to be displayed
    """

    decoration = '~'*(len(message)+4)
    print(decoration)
    print(message.center(len(message)+4))
    print(decoration)


def confirm_argument_is_number(* numbers, is_a_variable:bool=True):
    """Checks if the given argument is a number

    Args:
        is_a_variable (bool, optional): _description_. Defaults to True.

    Raises:
        TypeError: _description_

    Returns:
        _type_: _description_
    """
    try:
        if is_a_variable:
            for number in numbers:
                number = float(number)
        else:
            for number_list in numbers:
                for number in number_list:
                    number = float(number)

    except ValueError:
        raise TypeError('The arguments must be numbers (integers or floats)')

    return True


def calculate_area(square_width, square_height):
    """Multiplies width by height and returns the area

    Args:
        square_width (float): Square width size
        square_height (float): Square height size

    Returns:
        float: Square area
    """

    confirm_argument_is_number(square_height, square_width)

    square_area = square_width * square_height
    return square_area


def tell(initial_number: int, final_number: int, jump_numbers: int):
    """Counts from start to finish, skipping each step

    Args:
        initial_number (integer): Number starting the count
        final_number (integer): Number ending the count
        jump_numbers (integer): Number of numbers you will skip at each counting step
    """

    confirm_argument_is_number(initial_number, final_number, jump_numbers)

    print(f'Contagem de {initial_number} até {
          final_number} de {jump_numbers} em {jump_numbers}')

    counting = initial_number

    if jump_numbers < 0:
        jump_numbers *= -1
    if jump_numbers == 0:
        jump_numbers = 1

    if initial_number < final_number:
        while counting <= final_number:
            print(f'{counting}', end=' ')
            counting += jump_numbers
            sleep(0.2)
    else:
        while counting >= final_number:
            print(f'{counting}', end=' ')
            counting -= jump_numbers
            sleep(0.2)
    print()


def show_greater_value(* numbers: tuple):
    """Shows the largest number in the list of typed numbers

    Args:
    numbers (tuple): Numbers a se
    """

    confirm_argument_is_number(numbers, False)

    print(f'O maior número entre os {
          len(numbers)} números ({numbers}) é {max(numbers)}')


def generate_random_numbers(random_numbers_list: list):
    """Generates random numbers and adds them to a list

    Args:
        random_numbers_list (list): List to which the numbers will be added
    """

    for iterator in range(5):
        random_numbers_list.append(randint(1, 100))


def add_up_the_even_numbers(numbers_list: list):
    """Sum the even numbers in a list

    Args:
        numbers_list (list): List that will have its even numbers added together

    Returns:
        float: Sum of all even numbers in the list
    """

    evens = 0

    for number in numbers_list:
        if number % 2 == 0:
            evens += number

    return evens
