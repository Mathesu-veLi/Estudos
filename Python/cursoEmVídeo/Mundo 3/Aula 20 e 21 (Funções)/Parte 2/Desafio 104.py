def lerNúmero(mensagemDoInput):
    while True:
        número = str(input(mensagemDoInput))
        if número.isnumeric() == False:
            print('Digite somente números por favor!')
        else:
            número = int(número)
            break
    return número

print(f'Você digitou o número {lerNúmero("Digite um número: ")}')