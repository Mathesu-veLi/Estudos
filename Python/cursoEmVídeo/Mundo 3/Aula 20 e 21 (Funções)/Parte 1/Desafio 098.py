from modules import tell


tell(1, 10, 1)
tell(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')

while True:
    try:
        start = int(input('Inicio: '))
        end = int(input('Fim: '))
        step = int(input('Passo: '))
        break
    except ValueError:
        print('Dígite somente números por favor')

tell(start, end, step)
print('Fim!')
