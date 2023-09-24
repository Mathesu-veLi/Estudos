soma = quantidadeDeNúmeros = 0
número = int(input('Digite um número (Digite 999 para sair do programa): '))
while número != 999:
    soma += número
    quantidadeDeNúmeros += 1
    número = int(input('Digite outro número: '))
print(f'Foram digitados {quantidadeDeNúmeros} números e a soma desses valores é {soma}')
