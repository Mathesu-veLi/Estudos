const { lookahead } = require('./base');

// Positive lookahead
const regExPositive = /.+(?=[^in]active)/gm;

// Negative lookahead
const regExNegative = /^(?!.+[^in]active).+$/gm;

//console.log(lookahead);

console.log(lookahead.match(regExPositive));

console.log(lookahead.match(regExNegative));
