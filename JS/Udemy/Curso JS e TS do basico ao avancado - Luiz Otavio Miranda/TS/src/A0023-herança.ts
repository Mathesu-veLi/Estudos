export class Pessoa {
    constructor(
        public readonly nome: string,
        public readonly sobrenome: string,
        private idade: number,
        protected readonly cpf: string,
    ) {}

    getIdade(): number {
        return this.idade;
    }

    getCpf(): string {
        return this.cpf;
    }

    getNomeCompleto(): string {
        return `${this.nome} ${this.sobrenome}`;
    }
}
