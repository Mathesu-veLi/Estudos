entered_weights = []
for iterator in range(1, 6):
    weight_of_person = float(input(f'Qual o peso da {iterator}° pessoa?: '))
    entered_weights.append(weight_of_person)
    
print(f'O menor peso lido foi {min(entered_weights)}kg e o maior foi {max(entered_weights)}kg')