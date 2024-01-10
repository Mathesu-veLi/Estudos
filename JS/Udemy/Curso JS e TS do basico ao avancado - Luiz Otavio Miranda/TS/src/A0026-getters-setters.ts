export class Pessoa {
    constructor(
        private nome: string,
        private sobrenome: string,
        private idade: number,
        private _cpf: string,
    ) {}

    set cpf(cpf: string) {
        this.cpf = valor;
        this._cpf = cpf;
    }

    get cpf(): string {
        return this._cpf.replace(/\D/g, '');
    }
}

const pessoa = new Pessoa('Luiz', 'Miranda', 30, '000.000.0000-00');
pessoa.cpf = '123.456.789.99';
console.log(pessoa.cpf);
