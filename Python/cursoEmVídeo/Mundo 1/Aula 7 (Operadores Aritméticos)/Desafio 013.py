salary = float(input('Qual seu salário?: R$'))
salary_with_increase = (salary * 0.15) + salary
print(
    f'Se você recebesse 15% de aumento, receberia R${salary_with_increase:.2f}')
