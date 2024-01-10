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

export class Cliente extends Pessoa {
    getNomeCompleto(): string {
        console.log('Fazendo algo antes');
        const result = super.getNomeCompleto();
        return result + '';
    }
}
export class Aluno extends Pessoa {
    constructor(
        nome: string,
        sobrenome: string,
        idade: number,
        cpf: string,
        public sala: string,
    ) {
        super(nome, sobrenome, idade, cpf);
    }

    getNomeCompleto(): string {
        return `Isso vem do aluno: ${this.nome} ${this.sobrenome}`;
    }
}

const pessoa = new Pessoa('Matheus', 'Silva', 30, '000.000.000-00');
const cliente = new Cliente('Maria', 'Veríssimo', 20, '111.111.111-11');
const aluno = new Aluno('Luiz', 'Miranda', 40, '222.222.222-22');

console.log(pessoa.getNomeCompleto());
console.log(aluno.getNomeCompleto());
console.log(cliente.getNomeCompleto());
