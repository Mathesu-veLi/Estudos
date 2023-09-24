contaEscolhida = 0
primeiroNúmero = int(input('Digite um número: '))
segundoNúmero = int(input('Digite outro número: '))
while contaEscolhida != 5:
    
    print('Oque você quer fazer com esses números? Digite: ')
    contaEscolhida = int(input('''
    [1] para somar
    [2] para multiplicar
    [3] para saber qual o maior
    [4] para digitar novos números
    [5] para sair do programa
    Escolha: '''))
    
    if contaEscolhida == 1:
        resultadoDaSoma = primeiroNúmero + segundoNúmero
        print(f'A soma dos números {primeiroNúmero} e {segundoNúmero} é {resultadoDaSoma}')
    
    elif contaEscolhida == 2:
        resultadoDaMultiplicação = primeiroNúmero * segundoNúmero
        print(f'O produto da multiplicação entre os números {primeiroNúmero} e {segundoNúmero} é {resultadoDaMultiplicação}')
    
    elif contaEscolhida == 3:
        if primeiroNúmero > segundoNúmero:
            print(f'O maior valor digitado foi {primeiroNúmero}')
        else:
            print(f'O maior valor digitado foi {segundoNúmero}')
    
    elif contaEscolhida == 4:
        print('Informe os números novamente: ')
        primeiroNúmero = int(input('Digite um número: '))
        segundoNúmero = int(input('Digite outro número: '))
    
    elif contaEscolhida > 5:
        print('Escolha inválida, tente novamente')
print('Programa finalizado')