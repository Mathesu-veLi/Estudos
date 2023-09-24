// For in -> lê os índices do objeto

/*const frutas = ['Pera', 'Maçã', 'Uva'];

//for (let i = 0; i < frutas.length; i++) {
//    console.log(frutas[i]);
//}

for (let índice in frutas) {
    console.log(frutas[índice]);
} */

const pessoa = {
    nome: 'Matheus',
    sobrenome: 'Levi',
    idade: 13
};

for (let chave in pessoa) {
    console.log(chave, pessoa[chave]);
}

console.log(pessoa.nome);