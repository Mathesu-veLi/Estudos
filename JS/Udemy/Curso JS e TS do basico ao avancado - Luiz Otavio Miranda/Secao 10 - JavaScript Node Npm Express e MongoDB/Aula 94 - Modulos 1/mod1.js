const nome = 'Luiz';
const sobrenome = 'Miranda';

const falaNome = () => {
    console.log(nome, sobrenome);
}
/*
module.exports.nome = nome;
module.exports.sobrenome = sobrenome;
module.exports.falaNome = falaNome;

console.log(module.exports);

exports.nome = nome;
exports.sobrenome = sobrenome;
exports.falaNome = falaNome;

this.qualquerCoisa = 'O que eu quiser exportar';*/

class Pessoa {
    constructor(nome) {
        this.nome = nome
    };
};

exports.Pessoa = Pessoa;

module.exports = {
    nome, sobrenome
};