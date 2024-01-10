export class Personagem {
    constructor(
        protected nome: string,
        protected ataque: number,
        protected vida: number,
    ) {}

    atacar(personagem: Personagem): void {
        console.log(`${this.nome} está atacando ${personagem.nome}`);
        personagem.perderVida(this.ataque);
    }

    perderVida(forcaAtaque: number): void {
        this.vida -= forcaAtaque;
        console.log(`${this.nome} agora tem ${this.vida}`);
    }
}

export class Guerreiro extends Personagem {}
export class Monstro extends Personagem {}

const guerreiro = new Guerreiro('Guerreiro', 10, 100);
const monstro = new Monstro('Monstro', 10, 1000);

guerreiro.atacar(monstro);
guerreiro.atacar(monstro);
guerreiro.atacar(monstro);
monstro.atacar(guerreiro);
