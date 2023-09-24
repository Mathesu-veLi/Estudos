número = int(input('Digite um número inteiro de 0 a 9999: '))
unidade = número // 1 % 10
dezena = número // 10 % 10
centena = número // 100 % 10
milhar = número // 1000 % 10
print(f'O número {número} tem\n {unidade} unidades, {dezena} dezenas, {centena} centenas e {milhar} milhares')