// g - global (encontra todas as ocorrências)
// i - insensitive (lower or upper case)

const { texto } = require('./base');

const regExp1 = /João/gi;

console.log(regExp1.test(texto));
