type Pessoa = {
    nome: string;
    idade: Idade;
    salario: number;
    corPreferida?: string;
}
type Idade = number;
type CorRGB = 'Vermelho' | 'Verde' | 'Azul';
type CorCMYK = 'Ciano' | 'Magenta' | 'Amarelo' | 'Preto';
type CorPreferida = CorRGB | CorCMYK;

const pessoa: Pessoa = {
    idade: 30,
    nome: 'Matheus',
    salario: 200_000,
}

export function setCorPreferida(pessoa: Pessoa, cor: CorPreferida): Pessoa {
    return { ...pessoa, corPreferida: cor };
}

console.log(setCorPreferida(pessoa, 'Azul'));
console.log(pessoa);
