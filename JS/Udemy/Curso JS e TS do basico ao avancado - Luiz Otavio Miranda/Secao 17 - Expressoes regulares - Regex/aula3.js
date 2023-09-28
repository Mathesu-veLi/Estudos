/*
  Quantificadores:
    * (opcional)
    + (obrigatório)
    ? (opcional)
*/

const { texto } = require('./base');

const regExp1 = /Jo+ão+/gi;

console.log(texto);
console.log(texto.match(regExp1));
