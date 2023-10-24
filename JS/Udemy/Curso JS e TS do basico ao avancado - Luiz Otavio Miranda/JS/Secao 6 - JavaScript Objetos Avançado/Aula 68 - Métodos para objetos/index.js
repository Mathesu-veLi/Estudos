const produto = { nome: 'Produto Base', preço: 1.8};
Object.freeze(produto);
produto.nome = 'Outro nome';
const caneca = Object.assign({}, produto, {material: 'porcelana'});

console.log(caneca);
console.log(produto);
Object.defineProperty(caneca, 'nome', {
    writable: false,
    configurable: false,
    value: 'Qualquer outra coisa'
})
console.log(Object.getOwnPropertyDescriptor(caneca, 'nome'));
console.log(Object.entries(produto));

for(let [chave, valor] of Object.entries(produto)) {
    console.log(chave, valor)
}