valores = list()
for c in range(0,5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > valores[-1]:
        valores.append(valor)
    else:
        posição = 0
        while posição < len(valores):
            if valor <= valores[posição]:
                valores.insert(posição, valor)
                break
            posição += 1
print(f'Os valores digitados e ordem foram {valores}')
    