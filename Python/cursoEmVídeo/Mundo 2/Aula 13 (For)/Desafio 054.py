from datetime import date
pessoasMaioresDeIdade = 0
pessoasMenoresDeIdade = 0
for c in range(1, 8):
    anoDeNascimento = int(input(f'Digite o ano de nascimento da {c}° pessoa: '))
    if anoDeNascimento <= date.today().year - 18:
        pessoasMaioresDeIdade += 1
    else:
        pessoasMenoresDeIdade += 1
print(f'{pessoasMaioresDeIdade} pessoas são maior de idade')
print(f'{pessoasMenoresDeIdade} pessoas são menor de idade')