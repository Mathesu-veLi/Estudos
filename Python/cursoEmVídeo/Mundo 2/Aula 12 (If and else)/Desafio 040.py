firstGrade = float(input('Digite a nota do 1° bimestre: '))
secondGrade = float(input('Agora a nota do 2° bimestre: '))
average = (firstGrade + secondGrade) / 2

print(f'Sua média foi {average}')

if average < 6:
    print('Você foi REPROVADO!')
else:
    print('Você foi APROVADO!')
