const { cpfs } = require('./base')

let regExp = /[\d{3,}]+.[\d{3,}]+.[\d{3,}]+-[\d{3,}]+/g;

console.log(cpfs.match(regExp))
