from time import sleep

def calcularFatorial(número, show=False):
    """-> Calcula o fatorial do número digitado

    Args:
        número (int): Número a se mostrar fatorial.
        show (bool, optional): Mostrar ou não o processo de fatoração do :param número:.
    """
    
    fatorial = número
    for c in range((número - 1), 0, -1):
        sleep(0.5)
        if show == True:
            if c == 1:
                print(fatorial)
            else:
                print(f'{fatorial} x {c} -> ', end='')
        fatorial *= c
    return fatorial 

número = int(input('Digite um número para ver seu fatorial: '))
print(f'O fatorial de {número} é {calcularFatorial(número, True)}')

