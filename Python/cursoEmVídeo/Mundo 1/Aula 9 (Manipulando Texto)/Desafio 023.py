number = int(input('Digite um número inteiro de 0 a 9999: '))
units = number // 1 % 10
dozens = number // 10 % 10
hundreds = number // 100 % 10
thousand = number // 1000 % 10
print(f'O número {number} tem\n {units} unidades, {dozens} dezenas, {hundreds} centenas e {thousand} milhares')