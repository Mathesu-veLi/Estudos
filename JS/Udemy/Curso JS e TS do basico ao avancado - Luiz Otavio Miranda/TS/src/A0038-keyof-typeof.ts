type CoresObj = typeof coresObj;

const coresObj = {
    vermelho: 'red',
    verde: 'green',
    azul: 'blue',
};

function traduzirCor(cor: 'vermelho' | 'verde' | 'azul', cores: CoresObj) {
    return cores[cor];
}

console.log(traduzirCor('vermelho', coresObj));
console.log(traduzirCor('verde', coresObj));
