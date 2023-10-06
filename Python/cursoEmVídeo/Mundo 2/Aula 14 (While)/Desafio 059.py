conta_escolhida = 0
primeiro_número = int(input('Digite um número: '))
segundo_número = int(input('Digite outro número: '))

while conta_escolhida != 5:

    print('Oque você quer fazer com esses números? Digite: ')
    conta_escolhida = int(input('''
    [1] para somar
    [2] para multiplicar
    [3] para saber qual o maior
    [4] para digitar novos números
    [5] para sair do programa
    Escolha: '''))

    if conta_escolhida == 1:
        resultado_da_soma = primeiro_número + segundo_número
        print(
            f'A soma dos números {primeiro_número} e {segundo_número} é {resultado_da_soma}')

    elif conta_escolhida == 2:
        resultadoDaMultiplicação = primeiro_número * segundo_número
        print(
            f'O produto da multiplicação entre os números {primeiro_número} e {segundo_número} é {resultadoDaMultiplicação}')

    elif conta_escolhida == 3:
        if primeiro_número > segundo_número:
            print(f'O maior valor digitado foi {primeiro_número}')
        else:
            print(f'O maior valor digitado foi {segundo_número}')

    elif conta_escolhida == 4:
        print('Informe os números novamente: ')
        primeiro_número = int(input('Digite um número: '))
        segundo_número = int(input('Digite outro número: '))

    elif conta_escolhida > 5:
        print('Escolha inválida, tente novamente')

print('Programa finalizado')
