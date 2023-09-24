contador = maisTermos = 1
termo = int(input('Digite o primeiro termo na PA: '))
razão = int(input('Agora digite a razão: '))

while contador <= 10: 
    print(f'O {contador}° termo dessa PA é {termo}')
    termo += razão
    contador += 1

while maisTermos > 0:
    maisTermos = int(input('Quantos termos você quer mostrar mais? (Digite 0 para encerrar o programa): '))
    for c in range(maisTermos):
        print(f'O {contador}° termo dessa PA é {termo}')
        termo += razão
        contador += 1
