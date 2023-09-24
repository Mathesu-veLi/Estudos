cidade = str(input('Qual o nome da sua cidade?: ')).lower().strip().split()
if 'santo' in cidade[0]:
    print('Então sua cidade tem o nome "Santo" em seu começo ne?')
else:
    print('Uma pena que sua cidade não tem o nome "Santo" no começo dela')