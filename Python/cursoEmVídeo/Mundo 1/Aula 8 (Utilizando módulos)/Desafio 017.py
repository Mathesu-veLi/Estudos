from math import hypot


catheto_opposite = float(input('Digite o cateto oposto: '))
catheto_adjacent = float(input('Digite agora o cateto adjacente: '))
print(f'A hipotenusa é {hypot(catheto_opposite, catheto_adjacent):.2f}')
