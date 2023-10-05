from math import sin, cos, tan

while True:
    angle = str(
        input('Digite um ângulo para ver seu seno, cosseno e tangente: '))
    angle = angle.replace('°', '')

    try:
        angle = float(angle)
        break
    except:
        print('Digite um valor válido (ex: 45)')

print(f'O seno de {angle:.2f}° é {sin(angle):.3f}')
print(f'O cosseno é {cos(angle):.3f}')
print(f'E o tangente é {tan(angle):.3f}')
