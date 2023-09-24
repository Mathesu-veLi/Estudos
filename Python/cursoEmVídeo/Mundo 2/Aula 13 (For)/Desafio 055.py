pesosLidos = []
for c in range(1, 6):
    pesoDaPessoa = float(input(f'Qual o peso da {c}° pessoa?'))
    pesosLidos.append(pesoDaPessoa)
print(f'O menor peso lido foi {min(pesosLidos)}kg e o maior foi {max(pesosLidos)}kg')