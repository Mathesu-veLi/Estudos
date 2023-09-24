contador = 1 
termo = int(input('Digite o primeiro termo na PA: '))
razão = int(input('Agora digite a razão: '))

while contador != 10: 
    print(f'O {contador}° termo dessa PA é {termo}')
    termo += razão
    contador += 1