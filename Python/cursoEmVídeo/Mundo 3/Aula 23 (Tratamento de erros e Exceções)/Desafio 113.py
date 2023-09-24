from modularização import lerNúmero

númeroInteiro = lerNúmero('Digite um número inteiro: ', '\033[31mERRO: digite um número inteiro valido!\033[m')
númeroDecimal = lerNúmero('Digite um número real (decimal): ', '\033[31mERRO: digite um número real (decimal) valido!\033[m', float)
print(f'O valor inteiro digitado foi {númeroInteiro} e o valor real digitado foi {númeroDecimal}')