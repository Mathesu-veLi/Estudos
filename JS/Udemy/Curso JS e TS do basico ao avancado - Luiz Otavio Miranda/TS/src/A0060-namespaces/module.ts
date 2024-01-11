/* eslint-disable @typescript-eslint/no-namespace */
namespace MeuNamespace {
    export class PessoaDoNamespace {
        constructor(public nome: string) {}
    }

    const pessoa = new PessoaDoNamespace('Luiz');
    console.log(pessoa);

    export namespace OutroNamespace {
        export const nome = 'Matheus';
    }
}

export const pessoa = new MeuNamespace.PessoaDoNamespace('Luiz');
console.log(pessoa);
console.log(MeuNamespace.OutroNamespace.nome);
