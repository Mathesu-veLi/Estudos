import modules
import time

while True:
    modules.decorate_string('Menu Principal')

    print("1 - Ver pessoas cadastradas")
    print("2 - Cadastrar nova pessoa")
    print("3 - Sair do Sistema", '\n')
    option = modules.verify_choice(
        'Sua opção: ', 3, 'Digite um número valido!')

    match(option):
        case 1:
            modules.decorate_string('Pessoas cadastradas')
            try:
                registration_file = open("registers.txt", "r")
                print(registration_file.read())

            except FileNotFoundError:
                modules.decorate_string('Cadastre alguém primeiro!')

            time.sleep(1)

        case 2:
            while True:
                name = str(input('\nQual o nome?: '))
                age = modules.read_number(
                    'Qual a idade?: ', 'Digite uma idade valida!')

                modules.Person(name, age)

                to_continue = modules.confirm_if_it_will_continue(
                    'Quer continuar?')
                if not to_continue:
                    break

        case 3:
            modules.decorate_string('Volte sempre!')
            break
