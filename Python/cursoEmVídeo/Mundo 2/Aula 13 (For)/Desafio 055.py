enteredWeights = []
for quantifier in range(1, 6):
    weightOfPerson = float(input(f'Qual o peso da {quantifier}° pessoa?'))
    enteredWeights.append(weightOfPerson)
    
print(f'O menor peso lido foi {min(enteredWeights)}kg e o maior foi {max(enteredWeights)}kg')