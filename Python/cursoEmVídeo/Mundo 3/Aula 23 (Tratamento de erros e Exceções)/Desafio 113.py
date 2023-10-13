from modules import read_number

integer_number = read_number(
    'Digite um número inteiro: ', 'ERRO: digite um número inteiro valido!')
floating_number = read_number('Digite um número real (decimal): ',
                              'ERRO: digite um número real (decimal) valido!', float)
print(f'O valor inteiro digitado foi {
      integer_number} e o valor real digitado foi {floating_number}')
