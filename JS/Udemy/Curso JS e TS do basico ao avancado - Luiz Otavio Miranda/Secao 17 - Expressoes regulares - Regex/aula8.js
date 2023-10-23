const { html2 } = require('./base');

// $1 $2 $3 <- Retrovisores \1

const regEx = /(<(\w+)(?:[\s\S]*?)>)([\s\S]*?)(<\/\2>)/g

console.log(html2)
console.log(html2.replace(regEx, '$1"$3"$4'))
