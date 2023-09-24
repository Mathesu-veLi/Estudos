média = 0

for c in range(1, 4):
    média += float(input(f'Digite aqui sua {c}° nota: '))
    
média /= 3

print(f'Sua média foi {média:.2f}!')

if média < 6:
    print('Você reprovou!')
else:
    print('Você passou!')