@inverteNomeECor('Valor1', 'Valor2')
export class Animal {
    constructor(
        public nome: string,
        public cor: string,
    ) {}
}

function inverteNomeECor(param1: string, param2: string) {
    return function <T extends new (...args: any[]) => any>(target: T): T {
        console.log('decorador recebeu', target);

        return class extends target {
            cor: string;
            nome: string;

            constructor(...args: any[]) {
                super(...args);
                this.nome = this.inverte(args[0]);
                this.cor = this.inverte(args[1]);
            }

            inverte(valor: string): string {
                return valor.split('').reverse().join('') + ' ' + param1 + ' ' + param2;
            }
        };
    };
}

const animal = new Animal('Levi', 'roxo');
console.log(animal);
