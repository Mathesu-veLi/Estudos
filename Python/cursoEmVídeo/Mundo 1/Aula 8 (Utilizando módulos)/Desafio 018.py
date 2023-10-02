from math import sin, cos, tan


angle = str(input('Digite um ângulo para ver seu seno, cosseno e tangente: '))
angle = angle.replace('°', '')

try:
    angle = float(angle)
except:
    print('Digite um valor válido (ex: 45)')

print(f'O seno de {angle:.2f}° é {sin(angle):.3f}\nO cosseno é {cos(angle):.3f}\nE o tangente é {tan(angle):.3f}')