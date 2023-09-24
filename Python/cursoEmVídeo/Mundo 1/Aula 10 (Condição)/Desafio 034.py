salário = float(input('Digite aqui seu salário: R$'))
if salário > 1250:
    aumento = salário * 0.10 + salário
    print(f'Seu salário com 10% de aumento ficaria R${aumento:.2f}')
else:
    aumento = salário * 0.15 + salário
    print(f'Seu salário com 15% de aumento ficaria R${aumento:.2f}')