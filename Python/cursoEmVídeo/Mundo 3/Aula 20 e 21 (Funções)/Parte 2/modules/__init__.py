from time import sleep


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


def check_voting_obligation(age: int):
    """Check if voting is compulsory, optional or if it is not possible to vote

    Args:
        age (int): age of the person wishing to vote

    Returns:
        str: obligatoriness of vote
    """

    if age >= 18 and age < 70:
        return 'OBRIGATÓRIO'
    elif age >= 70 or age >= 16 and age < 18:
        return 'OPCIONAL'
    else:
        return 'NEGADO'


def calculate_factorial(number, show_process=False):
    """Calculates number factorials

    Args:
        number (int): number to be calculated factorial
        show_process (bool, optional): Show numbers to be multiplied to get the factorial. Defaults to False.

    Returns:
        int: Factorial of the number
    """

    factorial = number
    for multiplier in range((number - 1), 0, -1):
        sleep(0.5)

        if show_process:
            if multiplier == 1:
                print(factorial)
            else:
                print(f'{factorial} x {multiplier} -> ', end='')

        factorial *= multiplier

    return factorial


def player_sheet(name_of_footballer=0, number_of_goals=0):
    """Show footballer's sheet

    Args:
        name_of_footballer (int, optional): name of the footballer whose sheet will be shown. Defaults to 0.
        number_of_goals (int, optional): number of goals the footballer has scored. Defaults to 0.
    """
    if name_of_footballer == '':
        name_of_footballer = '<unknown>'
    print(f'O jogador {name_of_footballer} fez {
          number_of_goals} gols no campeonato')


def register_grades():
    """Records the student's grades

    Returns:
        dict: grade data
    """

    registered_grades = {'Number of grades recorded': 0,
                         'Highest grade': 0, 'Lowest grade': 0, 'Average grade': 0}

    grades = []
    while True:
        grade = check_if_is_number('Digite a nota do aluno [999 para parar]: ')
        if grade == 999:
            break
        grades.append(grade)

    registered_grades["Number of grades recorded"] = len(grades)
    registered_grades["Highest grade"] = max(grades)
    registered_grades["Lowest grade"] = min(grades)
    registered_grades["Average grade"] = sum(grades) / len(grades)

    return registered_grades


def analyze_grade():
    """analyzes grade data and returns school status

    Returns:
       str: school situation
    """
    registered_grades = register_grades()

    if registered_grades['Average grade'] >= 7:
        registered_grades["School situation"] = 'Boa'

    elif registered_grades['Average grade'] > 5 and registered_grades['Average grade'] <= 6:
        registered_grades['School situation'] = 'Razoável'

    elif registered_grades['Average grade'] <= 5:
        registered_grades['School situation'] = 'Ruim'

    return registered_grades['School situation']


def show_documentation(command):
    """shows command documentation

    Args:
        command (str): command to be displayed documentation
    """
    print(help(command))
