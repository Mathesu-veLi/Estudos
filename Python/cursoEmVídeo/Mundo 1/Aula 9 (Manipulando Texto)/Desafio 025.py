nome = str(input('Digite seu nome completo: ')).lower().strip().split()
if 'silva' in nome:
    print('Seu nome tem "Silva"')
else:
    print('Seu nome não tem "Silva"')