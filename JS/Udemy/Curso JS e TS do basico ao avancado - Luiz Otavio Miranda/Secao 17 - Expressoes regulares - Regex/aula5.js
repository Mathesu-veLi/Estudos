const {alfabeto} = require('./base')

// [^] -> Negação
// [\w] -> [A-Za-z0-9_]
// [\d] -> [0_9]
// [\s] -> espaços

console.log(alfabeto);
console.log(alfabeto.match(/[A-z]+/g));
console.log(alfabeto.match(/[^A-Za-z]+/g));
console.log(alfabeto.match(/\S\D+/g))
