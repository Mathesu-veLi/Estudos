pairNumbers = []
for quantifier in range(1, 7):
    number = int(input(f'Digite o {quantifier}° número: '))
    if number % 2 == 0:
       pairNumbers.append(number)

print(f'Se somar-mos só os números pares que você digitou ({len(pairNumbers)}), teriamos o número {sum(pairNumbers)}') 