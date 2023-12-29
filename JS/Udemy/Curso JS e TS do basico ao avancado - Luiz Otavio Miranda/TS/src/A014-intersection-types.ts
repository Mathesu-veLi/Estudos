type TemNome = { nome: string };
type TemSobrenome = { sobrenome: string };
type TemIdade = { idade: number };
type Pessoa = TemNome & TemSobrenome & TemIdade;

type AB = 'A' | 'B';
type AC = 'A' | 'C';
type AD = 'A' | 'D';
type Intersecao  = AB & AC & AD;

export const pessoa: Pessoa = {
    idade: 30,
    nome: 'Matheus',
    sobrenome: 'Silva',
}

console.log(pessoa);
