reais_in_the_wallet = float(
    input('Quantos reais você tem na carteira esse exato momento?: R$'))
real_to_dollar = reais_in_the_wallet / 5.04
print(f'Podes trocar R${reais_in_the_wallet:.2f} por US${real_to_dollar:.2f}')
