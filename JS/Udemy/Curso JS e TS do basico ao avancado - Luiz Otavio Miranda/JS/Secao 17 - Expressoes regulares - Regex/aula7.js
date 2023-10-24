const { cpfs } = require('./base');

// ^ -> Começa com
// $ -> Termina com
// [^] -> Negação
// m -> multiline

let regExp = /^(\d{3}\.){2}\d{3}\-\d{2}$/gm;
const cpf = "209.721.825-35"

console.log(cpfs)
console.log(cpfs.match(regExp))
console.log(cpf.match(regExp))
