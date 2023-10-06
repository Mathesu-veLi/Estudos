counter = more_terms = 1

term = int(input('Digite o primeiro termo na PA: '))
reason = int(input('Agora digite a razão: '))

while counter <= 10:
    print(f'O {counter}° termo dessa PA é {term}')
    term += reason
    counter += 1

while more_terms > 0:
    while True:
        more_terms = str(input(
            'Quantos termos você quer mostrar mais? (Digite 0 para encerrar o programa): '))
        try:
            more_terms = int(more_terms)
            break
        except:
            print('Digite um número!')

    for c in range(more_terms):
        print(f'O {counter}° termo dessa PA é {term}')
        term += reason
        counter += 1
