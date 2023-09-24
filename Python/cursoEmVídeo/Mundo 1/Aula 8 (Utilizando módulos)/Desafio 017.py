from math import hypot


catetoOposto = float(input('Digite o cateto oposto: '))
catetoAdjacente = float(input('Digite agora o cateto adjacente: '))
print(f'A hipotenusa é {hypot(catetoOposto, catetoAdjacente):.2f}')