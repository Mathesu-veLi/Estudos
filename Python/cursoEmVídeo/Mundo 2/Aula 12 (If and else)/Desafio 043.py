person = {
    'height': float(input('Qual sua altura?: ')),
    'weight': float(input('Qual seu peso?: ')),
}
person['body_mass_index'] = person['weight'] / (person['height'] ** 2)

print(f'Seu IMC é {person["body_mass_index"]:.2f}')

print('Você está ', end='')
if 18.5 > person["body_mass_index"]:
    print('Abaixo do peso')
elif 18.5 <= person["body_mass_index"] and person["body_mass_index"] < 25:
    print('no Peso Ideal')
elif 25 <= person["body_mass_index"] and person["body_mass_index"] < 30:
    print('Sobrepeso')
elif 30 <= person["body_mass_index"] and person["body_mass_index"] < 40:
    print('em Obesidade')
elif 40 <= person["body_mass_index"]:
    print('em Obesidade mórbida')
