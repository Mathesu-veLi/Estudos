total = nomeDoProdutoMaisBarato = produtosComMaisDe1000Reais = 0
preçoDoProdutoMaisBarato = ''

while True:
    nomeDoProduto = str(input('Digite o nome do produto: '))
    preçoDoProduto = float(input('Digite o preço dele: R$'))
    total += preçoDoProduto
    if total == preçoDoProduto:
        preçoMaisBarato = preçoDoProdutoMaisBarato = preçoDoProduto
        nomeDoProdutoMaisBarato = nomeDoProduto
    if preçoDoProduto > 1000:
        produtosComMaisDe1000Reais += 1
    if preçoDoProduto < preçoMaisBarato:
        nomeDoProdutoMaisBarato = nomeDoProduto
        preçoDoProdutoMaisBarato = preçoDoProduto
        
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N]: ')).upper()
    if 'N' in cont:
        break
print(f'O total gasto na compra foi de R${total:.2f}')
if produtosComMaisDe1000Reais != 0:
    print(f'{produtosComMaisDe1000Reais} produtos custam mais de R$1000')
print(f'E o(a) {nomeDoProdutoMaisBarato} é o produto mais barato, custando apenas R${preçoDoProdutoMaisBarato:.2f}')