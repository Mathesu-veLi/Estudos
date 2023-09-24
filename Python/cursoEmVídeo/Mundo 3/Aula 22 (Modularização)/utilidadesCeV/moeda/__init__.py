def incrementarPreço(preço, porcentagem, formatar=True):
    preço = ((preço / 100) * porcentagem) + preço
    if formatar == True:
        preço = formatarParaPreço(preço)
    return preço

def reduzirPreço(preço, porcentagem, formatar=True):
    preço = preço - ((preço / 100) * porcentagem)
    if formatar == True:
        preço = formatarParaPreço(preço)
    return preço

def dobrarPreço(preço, formatar=True):
    preço = preço * 2
    if formatar == True:
        preço = formatarParaPreço(preço)
    return preço
    
def diminuirPreçoPelaMetade(preço, formatar=True):
    preço = preço / 2
    if formatar == True:
        preço = formatarParaPreço(preço)
    return preço

def formatarParaPreço(preço, moeda='R$'):
    preço = '\033[32m' + f'{moeda}{preço:.2f}'.replace('.', ',') + '\033[m'
    return preço

def mostrarPreçoComAlterações(preço, porcentagemDeIncremento, porcentagemDeRedução):
    print('\033[m-' * 30)
    print('Resumo de valores'.center(30))
    print('-' * 30)
    print(f'Preço analizado:{f"{formatarParaPreço(preço)}":>22}')
    print(f'Dobro do preço:{f"{dobrarPreço(preço, True)}":>23}')
    print(f'Metade do preço:{f"{diminuirPreçoPelaMetade(preço, True)}":>22}')
    print(f'{porcentagemDeIncremento}% de aumento:{f"{incrementarPreço(preço, porcentagemDeIncremento, True)}":>23}')
    print(f'{porcentagemDeRedução}% de redução:{f"{reduzirPreço(preço, porcentagemDeRedução, True)}":>23}')
    print('-' * 30)
    