/*const pessoa = {
    nome: 'Matheus',
    sobrenome: 'Fernandes'
};

const chave = 'sobrenome';

console.log(pessoa.nome, pessoa[chave]);

const pessoa1 = new Object();
pessoa1.nome = 'Matheus';
pessoa1.sobrenome = 'Fernandes';
pessoa1.idade = 13;
pessoa1.falarNome = () => {
    console.log(`${pessoa1.nome} está falando seu nome`);
};
pessoa1.getDataDeNascimento = () => new Date().getFullYear() - pessoa1.idade;

pessoa1.falarNome();
console.log(`${pessoa1.nome} nasceu em ${pessoa1.getDataDeNascimento()}`);

for (let chave in pessoa1) {
    console.log(pessoa1[chave]);
}*/

/*const criaPessoa = (nome, sobrenome) => ({
    nome,
    sobrenome,
    get nomeCompleto() {
        return `${this.nome} ${this.sobrenome}`;
    }
})

const p1 = criaPessoa('Matheus', 'Fernandes')
console.log(p1.nomeCompleto)*/

function Pessoa(nome, sobrenome) {
    this.nome = nome;
    this.sobrenome = sobrenome;

    Object.freeze(this);
};

const p1 = new Pessoa('Matheus', 'Fernandes');
p1.nome = 'Outra pessoa';
const p2 = new Pessoa('Luiz', 'Miranda');
console.log(p1);
