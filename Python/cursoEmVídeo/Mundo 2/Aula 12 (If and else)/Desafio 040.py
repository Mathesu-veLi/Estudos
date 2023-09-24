primeiraNota = float(input('Digite a nota do 1° bimestre: '))
segundaNota = float(input('Agora a nota do 2° bimestre: '))
média = (primeiraNota + segundaNota) / 2
if média < 6:
    print('\033[31mREPROVADO\033[m')
else:
    print('\033[32mAPROVADO\033[m')
