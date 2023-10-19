const { cpfs } = require('./base')

let regExp = /(\d{3}\.){2}\d{3}\-\d{2}/g;

console.log(cpfs.match(regExp))
