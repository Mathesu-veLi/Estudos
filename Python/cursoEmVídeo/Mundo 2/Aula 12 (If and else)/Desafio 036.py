house = float(input('Digite o valor da casa que vc quer comprar: R$'))
salary = float(input('Digite quando você ganha por mês: R$'))
year = int(input('Agora digite em quantos anos você pretende pagar: '))
monthlyInstallments = house / (year * 12)

if monthlyInstallments > salary - (salary * 0.30):
    print('Status do Empréstimo: Negado')
else:
    print('Status do Empréstimo: Aprovado')
    print(f'Você tera que pagar R${monthlyInstallments:.2f} por mês')