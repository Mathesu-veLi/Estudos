@outroDecorador('param')
@inverteNomeECor('Valor1', 'Valor2')
export class Animal {
    constructor(
        public nome: string,
        public cor: string,
    ) {}
}

function inverteNomeECor(param1: string, param2: string) {
    return function (target: Constructor) {
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

function outroDecorador(param1: string) {
    return function (target: Constructor) {
        console.log('Sou outro decorador' + param1);
        return target;
    };
}

interface Constructor {
    new (...args: any[]): any;
}

const animal = new Animal('Levi', 'roxo');
console.log(animal);
