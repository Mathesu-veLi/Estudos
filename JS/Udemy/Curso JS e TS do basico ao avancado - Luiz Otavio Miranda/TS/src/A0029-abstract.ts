export abstract class Personagem {
    constructor(
        protected nome: string,
        protected ataque: number,
        protected vida: number,
    ) {}

    atacar(personagem: Personagem): void {
        this.bordao();
        personagem.perderVida(this.ataque);
    }

    perderVida(forcaAtaque: number): void {
        this.vida -= forcaAtaque;
        console.log(`${this.nome} agora tem ${this.vida}`);
    }

    abstract bordao(): void;
}

export class Guerreiro extends Personagem {
    bordao(): void {
        console.log('GUERREIRO atacando');
    }
}
export class Monstro extends Personagem {
    bordao(): void {
        console.log('MONSTRO atacando');
    }
}

const guerreiro = new Guerreiro('Guerreiro', 10, 100);
const monstro = new Monstro('Monstro', 10, 1000);

guerreiro.atacar(monstro);
guerreiro.atacar(monstro);
guerreiro.atacar(monstro);
monstro.atacar(guerreiro);
