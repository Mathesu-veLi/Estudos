export class Empresa {
    public readonly nome: string;
    protected readonly cnpj: string;

    constructor(nome: string, cnpj: string) {
        this.nome = nome;
        this.cnpj = cnpj;
    }
}

const empresa1 = new Empresa('Udemy');

const empresa1 = new Empresa('Udemy', '11.111.111/0001-11');
console.log(empresa1);
