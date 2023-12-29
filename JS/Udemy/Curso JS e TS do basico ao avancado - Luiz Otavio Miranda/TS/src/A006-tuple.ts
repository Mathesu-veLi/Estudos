const dadosCliente1: readonly [number, string] = [1, 'Matheus'];
const dadosCliente2: [number, string, string?] = [1, 'Matheus', 'Silva'];
const dadosCliente3: [number, string, ...string[]] = [1, 'Matheus', 'Levi', 'Fernandes', 'da Silva'];

console.log(dadosCliente1);
console.log(dadosCliente2);
console.log(dadosCliente3);

const array: readonly string[] = ['Matheus', 'Otávio'];
