interface PessoaProtocolo<T = string, U = number> {
    nome: T;
    sobrenome: T;
    idade: U;
}

const aluno1: PessoaProtocolo = {
    nome: 'Matheus',
    sobrenome: 'Levi',
    idade: 13,
};

const aluno2: PessoaProtocolo<string, number> = {
    nome: 'Matheus',
    sobrenome: 'Levi',
    idade: 13,
};

const aluno3: PessoaProtocolo<T = string, U = number> = {
    nome: 'Matheus',
    sobrenome: 'Levi',
    idade: 13,
};

console.log(aluno1);
console.log(aluno2);
console.log(aluno3);
