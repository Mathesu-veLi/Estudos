soma = 0
quantidadeDeValores = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        quantidadeDeValores += 1
        soma += c
print('A soma dos {} valores múltiplos de 3 de 0 a 500 é {}'.format(quantidadeDeValores, soma))