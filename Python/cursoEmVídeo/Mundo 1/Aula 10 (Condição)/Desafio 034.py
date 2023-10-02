salary = float(input('Digite aqui seu salário: R$'))

if salary > 1250:
    increase = (salary * 0.10) + salary
    print(f'Seu salário com 10% de aumento ficaria R${increase:.2f}')
else:
    increase = (salary * 0.15) + salary
    print(f'Seu salário com 15% de aumento ficaria R${increase:.2f}')