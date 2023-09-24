def mostrarDocumentação(comando):
    print(help(comando))

print('Digite o comando para ver sua documentação (stop para parar): ')
while True:
    comando = input('Função ou biblioteca: ')
    if comando.lower() == 'stop':
        break
    else:
        mostrarDocumentação(comando)