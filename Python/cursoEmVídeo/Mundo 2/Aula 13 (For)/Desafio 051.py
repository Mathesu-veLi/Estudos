termo = int(input('Digite o primeiro termo na PA: '))
razão = int(input('Agora digite a razão: '))
print(f'O 1° termo dessa PA é {termo}')
for c in range(2, 10): 
    termo = termo + razão
    print(f'O {c}° termo dessa PA é {termo}')
