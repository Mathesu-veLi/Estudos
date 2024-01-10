export class Empresa {
    public readonly nome: string;
    protected readonly colaboradores: Colaborador[] = [];
    protected readonly cnpj: string;

    constructor(nome: string, cnpj: string) {
        this.nome = nome;
        this.cnpj = cnpj;
    }

    public adicionaColaborador(colaborador: Colaborador): void {
        this.colaboradores.push(colaborador);
    }

    public mostrarColaboradores(): void {
        this.colaboradores.forEach((colaborador) => console.log(colaborador));
    }
}

export class Udemy extends Empresa {
    constructor() {
        super('Udemy', '11.111.111/0001-11');
    }

    popColaborador(): Colaborador {
        const colaborador = this.colaboradores.pop();
        if (colaborador) return colaborador;
        return null;
    }
}

export class Colaborador {
    constructor(
        public readonly nome: string,
        public readonly sobrenome: string,
    ) {}
}

const empresa1 = new Udemy();

const colaborador1 = new Colaborador('Matheus', 'Silva');
const colaborador2 = new Colaborador('Luiz', 'Otávio');
const colaborador3 = new Colaborador('João', 'Vieira');
empresa1.adicionaColaborador(colaborador1);
empresa1.adicionaColaborador(colaborador2);
empresa1.adicionaColaborador(colaborador3);
empresa1.adicionaColaborador({
    nome: 'Maria',
    sobrenome: 'Silva',
});
const colaboradorRemovido = empresa1.popColaborador();
console.log(colaboradorRemovido);
empresa1.mostrarColaboradores();
