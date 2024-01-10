export class Escritor {
    private _ferramenta: Ferramenta | null = null;

    constructor(private _nome: string) {}

    get nome(): void {
        return this.nome;
    }

    set ferramenta(ferramenta: Ferramenta | null) {
        this._ferramenta = ferramenta;
    }

    get ferramenta(): Ferramenta | null {
        return this._ferramenta;
    }

    escrever(): void {
        if (this.ferramenta === null) {
            console.log('Não posso escrever sem ferramenta');
            return;
        }

        this.ferramenta.escrever();
    }
}

export abstract class Ferramenta {
    constructor(private _name: string) {}
    abstract escrever(): void;

    get nome(): string {
        return this._name;
    }
}

export class Caneta extends Ferramenta {
    escrever(): void {
        console.log(`${this.nome} está escrevendo`);
    }
}

export class MaquinaEscrever extends Ferramenta {
    escrever(): void {
        console.log(`${this.nome} está escrevendo`);
    }
}

const escritor = new Escritor('Matheus');
const caneta = new Caneta('Bic');
// eslint-disable-next-line @typescript-eslint/no-unused-vars
const maquinaEscrever = new MaquinaEscrever('Máquina');

escritor.ferramenta = caneta;
escritor.escrever();
