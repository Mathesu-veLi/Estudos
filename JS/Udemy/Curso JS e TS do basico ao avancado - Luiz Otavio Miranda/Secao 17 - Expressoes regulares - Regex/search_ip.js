const { ips } = require('./base')

let regExp = /(\d+\.){3}\d+/g;

console.log(ips.match(regExp))
