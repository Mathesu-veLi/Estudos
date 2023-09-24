preço = float(input('Qual o valor do produto?: R$'))
total = preço
escolhaDePagamento = int(input('''Se você for pagar o produto:
    À vista no dinheiro/cheque (desconto de 10%), digite 1
    À vista no cartão (desconto de 5%), digite 2
    Em até 2x no cartão, digite 3
    Em 3x ou mais no cartão (com juros de 2% do valor total), digite 4
    Escolha: '''))
if escolhaDePagamento == 1:
    total = preço - (preço * 0.10)
elif escolhaDePagamento == 2:
    total = preço - (preço * 0.05)
elif escolhaDePagamento == 3:
    preçoDasParcelas = preço / 2
    print(f'Você vai pagar 2 parcelas de R${preçoDasParcelas:.2f} cada')
elif escolhaDePagamento == 4:
    quantidadeDeParcelas = int(input('Vai pagar em quantas parcelas?: '))
    total = preço + (preço * 0.2)
    preçoDasParcelas = total / quantidadeDeParcelas
    print(f'Você vai pagar em {quantidadeDeParcelas} parcelas de R${preçoDasParcelas:.2f} cada')
print(f'Você vai pagar R${total:.2f} no final')