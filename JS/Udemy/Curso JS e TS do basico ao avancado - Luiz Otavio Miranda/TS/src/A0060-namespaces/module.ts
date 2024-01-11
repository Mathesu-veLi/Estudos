/* eslint-disable @typescript-eslint/no-namespace */
namespace MeuNamespace {
    class PessoaDoNamespace {
        constructor(public nome: string) {}
    }

    const pessoa = new PessoaDoNamespace('Luiz');
    console.log(pessoa);
}
