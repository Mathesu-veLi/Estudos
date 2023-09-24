import urllib.request

try:
    urllib.request.urlopen('http://www.pudim.com.br')
except urllib.request.URLError:
    print('O site pudim.com.br não está disponível no momento')
else:
    print('Consegui acessar o site pudim.com.br')