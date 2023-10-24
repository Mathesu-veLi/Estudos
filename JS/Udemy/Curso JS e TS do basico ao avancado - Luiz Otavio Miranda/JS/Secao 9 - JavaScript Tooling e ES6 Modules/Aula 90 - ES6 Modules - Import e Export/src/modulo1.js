const nome = 'Matheus';
const sobrenome = 'Fernandes';
const idade = 30;

export function soma(x, y) {
    return x + y;
};

export default (x, y) => {
    return x * y
}

class Pessoa {
    constructor(nome, sobrenome) {
        this.nome = nome;
        this.sobrenome = sobrenome;
    };
};

export {nome, sobrenome, idade}