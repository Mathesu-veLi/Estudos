def lerNúmero(pergunta, mensagemDeErro='Digite somente números por favor!', tipo=int):
    """-> Só para de perguntar número ao usuário quando ele digita um número inteiro, impedindo assim que erros possam parar o programa

    Args:
        pergunta (str): Mensagem que irá aparecer no input
        mensagemDeErro (str, optional): Mensagem de erro que irá aparecer caso o valor informado não seja um número. Defaults to 'Digite somente números por favor!'.
        tipo (str, optional): Tipo de número que irá ser digitado (int ou float)
    """
    while True:
        global num
        num = str(input(pergunta)).strip()
        try:
            if tipo == int:
                num = int(num)
            elif tipo == float:
                if ',' in num:
                    num = num.replace(',', '.')
                num = float(num)
            return num
        except ValueError:
            print(mensagemDeErro)
            
def confirmarSeHaveráContinuação(pergunta):
    while True:
        continuar = input(f'{pergunta} [S/N]:').lower()
        if continuar not in 'sn':
            print('\033[31mErro! Digite S para continuar e N para parar\033[m')
        else:
            if 'n' in continuar:
                return False
            else:
                return True
            
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.cadastrarPessoa()
    def cadastrarPessoa(self):
        arquivoDeCadastros = open("cadastros.txt", "a")
        arquivoDeCadastros.write(f'\n\033[35m{self.nome}\033[m\t\t\t\033[36m{self.idade} anos\033[m')
    
def verificarEscolha(inputs, lim, errormsg):
    while True:
        num = int(input(inputs))
        if num > lim:
            print(errormsg)
        else:
            return num
def enfeitarTítulo(txt, numdevez):
    print('\033[m-' * numdevez)
    print(f"{txt}".center(numdevez))
    print('-' * numdevez)