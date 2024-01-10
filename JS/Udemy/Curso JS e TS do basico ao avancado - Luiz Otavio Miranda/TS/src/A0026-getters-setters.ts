export class Pessoa {
    constructor(
        private nome: string,
        private sobrenome: string,
        private idade: number,
        private cpf: string,
    ) {}

    setCpf(valor: string): void {
        this.cpf = valor;
    }

    getCpf(): string {
        return this.cpf.replace(/\D/g, '');
    }
}

const pessoa = new Pessoa('Luiz', 'Miranda', 30, '000.000.0000-00');
pessoa.setCpf('111.111.111-11');
console.log(pessoa.getCpf());
