city = str(input('Qual o nome da sua cidade?: ')).lower().strip().split()
if 'santo' in city[0]:
    print('Sua cidade tem \'Santo\' nela')
else:
    print('Uma pena que sua cidade não tem o nome \'Santo\' em seu nome')