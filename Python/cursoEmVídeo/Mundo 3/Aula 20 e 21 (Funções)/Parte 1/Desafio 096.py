def calcularÁrea(largura, comprimento):
    área = largura * comprimento
    return área


largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
print(f'A área de um terreno {largura:.2f} x {comprimento:.2f} é de {calcularÁrea(largura, comprimento)}m²')