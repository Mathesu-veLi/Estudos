function Pessoa(nome, sobrenome) {
    const ID = 123456;

    this.nome = nome;
    this.sobrenome = sobrenome;

    this.método = function() {
        console.log(this.nome + ': Sou um método')
    }
}

const p1 = new Pessoa('Matheus', 'Levi');
const p2 = new Pessoa('Maria', 'Oliveira');

console.log(p2.método());