term = int(input('Digite o primeiro termo na PA: '))
rate = int(input('Agora digite a razão: '))
print(f'O 1° termo dessa PA é {term}')

for quantifier in range(2, 10): 
    term = term + rate
    print(f'O {quantifier}° termo dessa PA é {term}')
