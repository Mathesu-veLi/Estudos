const pessoa = {
    nome: 'Matheus',
    //sobrenome: 'Fernandes',
    idade: 30,
    endereço: {
        rua: 'Av Brasil',
        numero: 320
    }
};

/*const {nome: teste, sobrenome = 'Não existe', idade, endereço: {rua: rua1, numero: numero1}} = pessoa;
console.log(teste, sobrenome, idade, rua1, numero1);*/

const {nome, sobrenome, ...resto} = pessoa;
console.log(nome, resto);