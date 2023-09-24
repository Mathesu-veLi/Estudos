valores = [[], []]
for c in range(0, 7):
    valor = int(input('Digite um número: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
valores[0].sort()
valores[1].sort()
print(f'Os valores pares digitados foram: {valores[0]}\nOs valores impares digitados foram: {valores[1]}')