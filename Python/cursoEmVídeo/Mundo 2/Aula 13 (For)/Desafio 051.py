term = int(input('Digite o primeiro termo na PA: '))
rate = int(input('Agora digite a razão: '))
print(f'O 1° termo dessa PA é {term}')

for iterator in range(2, 10):
    term = term + rate
    print(f'O {iterator}° termo dessa PA é {term}')
