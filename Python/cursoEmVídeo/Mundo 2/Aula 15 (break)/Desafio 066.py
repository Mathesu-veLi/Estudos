typed_numbers = []

while True:
    number = int(input('Digite um número (999 para parar): '))
    if number == 999:
        break
    typed_numbers.append(number)

print(f'A soma entre os {len(typed_numbers)} números digitados foi {sum(typed_numbers)}')