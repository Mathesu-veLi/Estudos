termos = int(input('Quantos termos você quer mostrar?: '))
contador = último = 0
penúltimo = 1
while contador != termos:
    número = último
    print(f'{número} -> ', end='')
    último = penúltimo + número
    penúltimo = número
    contador += 1
print('FIM')