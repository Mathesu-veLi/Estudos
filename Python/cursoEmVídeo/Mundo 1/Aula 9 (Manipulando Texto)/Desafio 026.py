phrase = str(input('Digite uma frase: ')).lower().strip()
print(f'A letra "a" (sem acento) aparece {phrase.count("a")} vezes na frase.')

if phrase.count("a") != 0:
    print(
        f'A letra "a" apareceu pela primeira vez na posição {phrase.find("a")}')
    print(f'A última letra "a" apareceu na posição {phrase.rfind("a")}')
