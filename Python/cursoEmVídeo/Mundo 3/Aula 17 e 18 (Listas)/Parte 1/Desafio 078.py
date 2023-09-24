valores = list()
for v in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(f'Os valores digitados foram:\n{valores}')
print(f'O maior valor digitado foi {max(valores)} na {valores.index(max(valores))}° posição e o menor foi {min(valores)} na {valores.index(min(valores))}° posição')