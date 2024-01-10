export class Pessoa {
    constructor(
        public nome: string,
        public sobrenome: string,
        public idade: number,
        public cpf: string,
    ) {}

    static falaOi(): void {
        console.log('Oi');
    }
}

const pessoa = new Pessoa('Luiz', 'Miranda', 30, '000.000.0000-00');
pessoa.cpf = '123.456.789.99';
console.log(pessoa);
Pessoa.falaOi();
