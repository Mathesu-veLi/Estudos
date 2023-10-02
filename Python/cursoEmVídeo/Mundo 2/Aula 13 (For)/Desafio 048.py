sum = 0
quantityOfValues = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        quantityOfValues += 1
        sum += c
        
print(f'A soma dos {quantityOfValues} valores múltiplos de 3 de 0 a 500 é {sum}')