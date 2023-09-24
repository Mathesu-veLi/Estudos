casa = float(input('Digite o valor da casa que vc quer comprar: R$'))
salário = float(input('Digite quando voce ganha por mes: R$'))
anos = int(input('Agora digite em quantos anos você pretende pagar: '))
parcelasMensais = casa / (anos * 12)

if parcelasMensais > salário - (salário * 0.30):
    print('Status do Empréstimo: Negado')
else:
    print('Status do Empréstimo: Aprovado')
    print(f'Você tera que pagar R${parcelasMensais:.2f} por mês')