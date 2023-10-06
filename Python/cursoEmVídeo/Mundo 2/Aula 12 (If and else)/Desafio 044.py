price_of_the_product = float(input('Qual o valor do produto?: R$'))
price_total_to_be_paid = price_of_the_product

form_of_payment = int(input('''Se você for pagar o produto:
    À vista no dinheiro/cheque (desconto de 10%), digite 1
    À vista no cartão (desconto de 5%), digite 2
    Em até 2x no cartão, digite 3
    Em 3x ou mais no cartão (com juros de 2% do valor total), digite 4
    Escolha: '''))

if form_of_payment == 1:
    price_total_to_be_paid = price_of_the_product - \
        (price_of_the_product * 0.10)

elif form_of_payment == 2:
    price_total_to_be_paid = price_of_the_product - \
        (price_of_the_product * 0.05)

elif form_of_payment == 3:
    price_of_installments = price_of_the_product / 2
    print(f'Você vai pagar 2 parcelas de R${price_of_installments:.2f} cada')

elif form_of_payment == 4:
    number_of_installments = int(input('Vai pagar em quantas parcelas?: '))
    price_total_to_be_paid = price_of_the_product + \
        (price_total_to_be_paid * 0.2)
    price_of_installments = price_total_to_be_paid / number_of_installments

    print(
        f'Você vai pagar em {number_of_installments} parcelas de R${price_of_installments:.2f} cada')

print(f'Você vai pagar R${price_total_to_be_paid:.2f} no final')
