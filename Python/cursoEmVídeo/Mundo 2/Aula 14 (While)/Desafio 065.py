confirmaçãoDeContinuação = 's'
médiaDosNúmeros = contador = 0
númerosDigitados = []

while 's' in confirmaçãoDeContinuação:
    número = int(input('Digite um valor: '))
    médiaDosNúmeros += número
    contador += 1
    númerosDigitados.append(número)
    confirmaçãoDeContinuação = str(input('Quer continuar? [S/N]: ')).lower().strip()

médiaDosNúmeros /= contador
print(f'O maior número digitado foi {max(númerosDigitados)} e o menor foi {min(númerosDigitados)}, e a media desses números é {médiaDosNúmeros:.2f}')
