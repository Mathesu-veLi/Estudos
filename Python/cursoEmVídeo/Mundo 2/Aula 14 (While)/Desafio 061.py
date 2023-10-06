counter = 1 
term = int(input('Digite o primeiro termo na PA: '))
reason = int(input('Agora digite a razão: '))

while counter != 10: 
    print(f'O {counter}° termo dessa PA é {term}')
    term += reason
    counter += 1