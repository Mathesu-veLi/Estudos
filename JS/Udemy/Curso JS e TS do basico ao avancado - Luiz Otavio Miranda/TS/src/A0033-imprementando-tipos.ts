export abstract class TipoPessoa {
    protected abstract nome: string;
    protected abstract sobrenome: string;
    protected abstract nomeCompleto(): string;
}

export class Pessoa extends TipoPessoa {
    constructor(
        protected nome: string,
        protected sobrenome: string,
    ) {
        super();
    }

    public nomeCompleto(): string {
        return `${this.nome} ${this.sobrenome}`;
    }
}

const pessoa = new Pessoa('Matheus', 'Silva');
console.log(pessoa.nomeCompleto());
