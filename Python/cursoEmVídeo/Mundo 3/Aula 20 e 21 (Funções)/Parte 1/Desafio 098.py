from time import sleep

def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    
    contagem = inicio
    
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    if inicio < fim:    
        while contagem <= fim:
            print(f'{contagem}', end=' ')
            contagem += passo
            sleep(0.2)
    else:
        while contagem >= fim:
            print(f'{contagem}', end=' ')
            contagem -= passo
            sleep(0.2)

    print('Fim!')
    

contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)