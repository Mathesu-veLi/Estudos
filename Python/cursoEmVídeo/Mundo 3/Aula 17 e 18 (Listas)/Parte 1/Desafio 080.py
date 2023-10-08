values = list()

for iterator in range(0,5):
    value = int(input('Digite um valor: '))
    if iterator == 0 or value > values[-1]:
        values.append(value)
    else:
        position = 0
        while position < len(values):
            if value <= values[position]:
                values.insert(position, value)
                break
            position += 1

print(f'Os valores digitados e ordem foram {values}')
    