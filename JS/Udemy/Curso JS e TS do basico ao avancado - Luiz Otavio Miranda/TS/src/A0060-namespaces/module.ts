/* eslint-disable @typescript-eslint/no-namespace */
namespace MeuNamespace {
    export class PessoaDoNamespace {
        constructor(public nome: string) {}
    }

    const pessoa = new PessoaDoNamespace('Luiz');
    console.log(pessoa);
}

export const pessoa = new MeuNamespace.PessoaDoNamespace('Luiz');
console.log(pessoa);
