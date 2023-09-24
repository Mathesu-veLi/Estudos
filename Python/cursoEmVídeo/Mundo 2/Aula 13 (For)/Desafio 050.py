númerosPares = []
for c in range(1, 7):
    número = int(input(f'Digite o {c}° número: '))
    if número % 2 == 0:
       númerosPares.append(número)
print(f'Se somar-mos só os números pares que você digitou ({len(númerosPares)}), daria {sum(númerosPares)}') 