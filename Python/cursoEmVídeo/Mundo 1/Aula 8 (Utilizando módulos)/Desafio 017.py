from math import hypot


cathetoOpposite = float(input('Digite o cateto oposto: '))
cathetoAdjacent = float(input('Digite agora o cateto adjacente: '))
print(f'A hipotenusa é {hypot(cathetoOpposite, cathetoAdjacent):.2f}')