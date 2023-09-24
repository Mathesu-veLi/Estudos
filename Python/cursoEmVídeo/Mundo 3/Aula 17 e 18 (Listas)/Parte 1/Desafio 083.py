expressão = str(input('Digite uma expressão numérica que use parênteses e eu verei se ele está fechado na ordem correta!:'))
quantidadeDeParenteses = []
for c in expressão:
    if c == '(' or ')':
        quantidadeDeParenteses.append(c)
if len(quantidadeDeParenteses) % 2 == 0:
    print('A expressão é valida')
else:
    print('A expressão é invalida!')