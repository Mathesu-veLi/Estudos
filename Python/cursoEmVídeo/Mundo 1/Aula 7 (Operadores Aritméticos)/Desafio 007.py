average = 0

for trimester in range(1, 4):
    average += float(input(f'Digite aqui sua {trimester}° nota: '))
average /= 3

print(f'Sua média foi {average:.2f}!')

if average < 6:
    print('Você reprovou!')
else:
    print('Você passou!')