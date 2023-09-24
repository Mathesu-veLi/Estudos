from random import randint

númerosSorteados = []

def sortearNúmeros():
    for c in range(5):
        númerosSorteados.append(randint(1, 100))

def somarNúmerosPares():
    pares = 0
    for c in númerosSorteados:
        if c % 2 == 0:
            pares += c
    return pares
    


sortearNúmeros()
print(f'Os números sorteados foram {númerosSorteados}')
print(f'A soma entre todos os números pares entre {númerosSorteados} tem o resultado de {somarNúmerosPares()}')