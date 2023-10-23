const { lookahead } = require('./base');

// Positive lookbehind
const regExPositive = /(?<=ONLINE\s+)\S+.*/gim;

// Negative lookbehind
const regExNegative = /^.+(?<!online.+)$/gim;

console.log(lookahead.match(regExPositive));

console.log(lookahead.match(regExNegative));
