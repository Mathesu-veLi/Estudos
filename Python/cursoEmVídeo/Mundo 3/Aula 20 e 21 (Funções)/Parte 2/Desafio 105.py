from modularização import lerNúmero

def registradorDeNotas():
    notasRegistradas = {'Quantidade de notas registradas': 0, 'Maior nota': 0, 'Menor nota': 0, 'Média de notas': 0}
    notas = []
    while True:
        nota = lerNúmero('Digite a nota do aluno [999 para parar]: ')
        if nota == 999:
            break
        notas.append(nota)
    notasRegistradas["Quantidade de notas registradas"] = len(notas)
    notasRegistradas["Maior nota"] = max(notas)
    notasRegistradas["Menor nota"] = min(notas)
    notasRegistradas["Média de notas"] = sum(notas) / len(notas)
    return notasRegistradas

def analisadorDeNotas():
    '''
        -> Pergunta a nota de alunos e coloca em um dicionario a quantidade de notas digitadas, a nota maxima digitada, a nota minima, a media das notas e a situação
    '''
    notasRegistradas = registradorDeNotas()
    if notasRegistradas['Média de notas'] >= 7:
        notasRegistradas["Situação escolar"] = 'Boa'
    elif notasRegistradas['Média de notas'] > 5 and notasRegistradas['Média de notas'] <= 6:
        notasRegistradas['Situação escolar'] = 'Razoável'
    elif notasRegistradas['Média de notas'] <= 5:
        notasRegistradas['Situação escolar'] = 'Ruim'
    return notasRegistradas['Situação escolar']
        
print(f'Sua situação escolar é: {analisadorDeNotas()}')
