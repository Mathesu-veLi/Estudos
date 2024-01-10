interface Pessoa {
    nome: string;
}

interface Pessoa {
    readonly sobrenome: string;
}

interface Pessoa {
    readonly enderecos: string[];
}

interface Pessoa {
    readonly idade?: number;
}

const pessoa: Pessoa = {
    nome: 'Luiz',
    sobrenome: 'Miranda',
    enderecos: ['Av. Brasil'],
};

console.log(pessoa);
