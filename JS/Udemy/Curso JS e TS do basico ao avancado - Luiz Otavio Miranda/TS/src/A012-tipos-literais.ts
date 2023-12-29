export let x = 10;
let a = 100 as const;

const pessoa = {
    nome: 'Matheus' as const,
    sobrenome: 'Silva'
}

function escolhaCor(cor: 'Vermelho' | 'Verde' | 'Azul') {
    return cor;
}

console.log(escolhaCor);
