priceOfTheProduct = float(input('Qual o valor do produto?: R$'))
priceTotalToBePaid = priceOfTheProduct

formOfPayment = int(input('''Se você for pagar o produto:
    À vista no dinheiro/cheque (desconto de 10%), digite 1
    À vista no cartão (desconto de 5%), digite 2
    Em até 2x no cartão, digite 3
    Em 3x ou mais no cartão (com juros de 2% do valor total), digite 4
    Escolha: '''))

if formOfPayment == 1:
    priceTotalToBePaid = priceOfTheProduct - (priceOfTheProduct * 0.10)
    
elif formOfPayment == 2:
    priceTotalToBePaid = priceOfTheProduct - (priceOfTheProduct * 0.05)
    
elif formOfPayment == 3:
    priceOfInstallments = priceOfTheProduct / 2
    print(f'Você vai pagar 2 parcelas de R${priceOfInstallments:.2f} cada')

elif formOfPayment == 4:
    numberOfInstallments = int(input('Vai pagar em quantas parcelas?: '))
    priceTotalToBePaid = priceOfTheProduct + (priceTotalToBePaid * 0.2)
    priceOfInstallments = priceTotalToBePaid / numberOfInstallments
    
    print(f'Você vai pagar em {numberOfInstallments} parcelas de R${priceOfInstallments:.2f} cada')
    
print(f'Você vai pagar R${priceTotalToBePaid:.2f} no final')