reta1 = float(input('Digite o comprimento da 1° reta: '))
reta2 = float(input('Digite o comprimento da 2° reta: '))
reta3 = float(input('Digite o comprimento da 3° reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Dá para fazer um triangulo com essas retas')
else:
    print('Não dá para fazer um triangulo com essas retas')