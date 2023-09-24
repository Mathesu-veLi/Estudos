from datetime import datetime as date

informaçõesTrabalhistas = {'nome': input('Qual seu nome?: '), 
        'anoDeNascimento': int(input('Em qual ano você nasceu?: ')),
        'idade': date.now().year, 
        'númeroDaCarteiraDeTrabalho': input('Digite o número de sua carteira de trabalho (0 se não tem): ')}
informaçõesTrabalhistas['idade'] = informaçõesTrabalhistas['idade'] - informaçõesTrabalhistas['anoDeNascimento']

if informaçõesTrabalhistas['númeroDaCarteiraDeTrabalho'] != "0":
    informaçõesTrabalhistas['ano de contratação'] = int(input('Em que ano você foi contratado?: '))
    informaçõesTrabalhistas['salário'] = float(input('Qual seu salário?: R$'))
    informaçõesTrabalhistas['aposentadoria'] = (informaçõesTrabalhistas['idade'] + informaçõesTrabalhistas['ano de contratação'] + 20) - date.now().year
    
for k, v in informaçõesTrabalhistas.items():
    print(f'{k.capitalize()} recebe {v}')
