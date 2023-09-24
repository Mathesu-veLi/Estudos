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