/*
  Quantificadores:
    * (opcional)
    + (obrigatório)
    ? (opcional)
    \ Caractere de escape
*/

const { texto, arquivos } = require('./base');

const regExp1 = /Jo+ão+/gi;

console.log(texto);
console.log(texto.match(regExp1));

const regExp2 = /\.(jpg|jpeg)/gi;

for (const arquivo of arquivos) {
  console.log('');
  console.log(arquivo, arquivo.match(regExp2));
}
