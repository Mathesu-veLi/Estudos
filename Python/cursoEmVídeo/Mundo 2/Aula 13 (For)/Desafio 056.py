from math import floor

médiaEntreAsIdades = maiorIdadeDentreOsHomens = mulheresMaioresDe20Anos = 0
nomeDoHomemMaisVelho = ''

for p in range(1, 5):
    print(f'{p}° pessoa')
    
    nomeDaPessoaAtual = str(input('Nome: ')).strip().capitalize()
    idadeDaPessoaAtual = int(input('Idade: '))
    sexoDaPessoaAtual = str(input('Sexo [M/F]: ')).lower().strip()
    médiaEntreAsIdades += idadeDaPessoaAtual
    
    if p == 1 and 'm' in sexoDaPessoaAtual:
        maiorIdadeDentreOsHomens = idadeDaPessoaAtual
        nomeDoHomemMaisVelho = nomeDaPessoaAtual
    elif sexoDaPessoaAtual == 'm' and idadeDaPessoaAtual > maiorIdadeDentreOsHomens:
        maiorIdadeDentreOsHomens = idadeDaPessoaAtual
        nomeDoHomemMaisVelho = nomeDaPessoaAtual
    if 'f' in sexoDaPessoaAtual and idadeDaPessoaAtual > 20:
        mulheresMaioresDe20Anos += 1

médiaEntreAsIdades /= 4
print(f'A media da idade do grupo é de {floor(médiaEntreAsIdades)} anos (arredondado para baixo)')
print(f'O homem mais velho tem {maiorIdadeDentreOsHomens} anos e o nome dele é {nomeDoHomemMaisVelho}')
print(f'E ao todo, são {mulheresMaioresDe20Anos} mulheres com menos de 20 anos')