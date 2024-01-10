export abstract class Personagem {
    protected abstract emoji: string;

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
        console.log(`${this.emoji} - ${this.nome} agora tem ${this.vida}`);
    }

    abstract bordao(): void;
}

export class Guerreiro extends Personagem {
    protected emoji = '\u{1F9DD}';

    bordao(): void {
        console.log('GUERREIRO atacando');
    }
}
export class Monstro extends Personagem {
    protected emoji = '\u{1F9DF}';

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
