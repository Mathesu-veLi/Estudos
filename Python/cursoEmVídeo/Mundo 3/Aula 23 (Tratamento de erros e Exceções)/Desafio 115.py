import modularização, time

while True:
    modularização.enfeitarTítulo('Menu Principal', 31)
    
    print('''\033[33m1\033[m - \033[34mVer pessoas cadastradas\033[m
\033[33m2\033[m - \033[34mCadastrar nova pessoa\033[m
\033[33m3\033[m - \033[34mSair do Sistema\n\033[m''')
    
    opção = modularização.verificarEscolha('\033[32mSua opção: ', 3, '\033[31mDigite um número valido!\033[m')
    if opção == 1:
        modularização.enfeitarTítulo('Pessoas cadastradas', 31)
        try:
            arquivoComCadastros = open("cadastros.txt", "r")
            print(arquivoComCadastros.read())
        except FileNotFoundError:
            print('\033[31m',end='')
            print('Cadastre alguém primeiro!'.center(31),end='')
            print('\033[m')
        time.sleep(1)
    if opção == 2:
        while True:
            nome = str(input('\033[m\nQual o nome?: '))
            idade = modularização.lerNúmero('Qual a idade?: ', 'Digite uma idade valida!')
            modularização.Pessoa(nome, idade)
            continuar = modularização.confirmarSeHaveráContinuação('Quer continuar?')
            if continuar == False:
                break
    if opção == 3:
        modularização.enfeitarTítulo('Volte sempre!')
        break