const nomes = ['Maria', 'João', 'Eduardo', 'Gabriel', 'Júlia'];

// nomes.splice(índice, delete, elemento...)
const removidos = nomes.splice(-1, 1, 'Luiz', 'Carlos');

console.log(nomes);
console.log(removidos);