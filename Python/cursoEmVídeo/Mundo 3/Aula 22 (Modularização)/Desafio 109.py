from utilidadesCeV import moeda

preço = float(input('Digite o preço: \033[032mR$'))
preçoFormatado = moeda.formatarParaPreço(preço)
print(f'\033[mA metade de {preçoFormatado} é {moeda.diminuirPreçoPelaMetade(preço)}')
print(f'O dobro de {preçoFormatado} é {moeda.dobrarPreço(preço)}')
print(f'Aumentando 10%, temos {moeda.incrementarPreço(preço, 10)}')
print(f'Reduzindo 13%, temos {moeda.reduzirPreço(preço, 13)}')
