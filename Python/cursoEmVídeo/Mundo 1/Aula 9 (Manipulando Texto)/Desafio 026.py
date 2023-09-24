frase = str(input('Digite uma frase: ')).lower().strip()
print(f'A letra "a" aparece {frase.count("a")} vezes na frase.')
print(f'A letra apareceu na posição {frase.find("a")+1}'.format())
print(f'A última letra "a" apareceu na posição {frase.rfind("a")+1}')