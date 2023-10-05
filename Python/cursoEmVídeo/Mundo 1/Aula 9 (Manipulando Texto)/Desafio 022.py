name = input('Digite aqui seu nome completo: ').strip()

print(f'Seu nome com todas as letras maiúsculas fica {name.upper()}')
print(f'Seu nome com todas as letras minusculas fica {name.lower()}')
print(f'Seu nome tem ao todo {len(name) - name.count(" ")} letras')

name_separate = name.split()
print(
    f'Seu primeiro nome é {name_separate[0]} e ele tem {len(name_separate[0])} letras')
