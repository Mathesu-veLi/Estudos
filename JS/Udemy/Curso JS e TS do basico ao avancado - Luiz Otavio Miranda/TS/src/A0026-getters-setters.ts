export class Pessoa {
    constructor(
        private readonly nome: string,
        private readonly sobrenome: string,
        private idade: number,
        private cpf: string,
    ) {}

    getNome(): string {
        return this.nome;
    }

    getCpf(): string {
        return this.cpf.replace(/\D/g, '');
    }
}

const pessoa = new Pessoa('Luiz', 'Miranda', 30, '000.000.0000-00');
console.log(pessoa.getCpf());
