/*const objetoA = {
    chaveA: 'A'
};

const objetoB = {
    chaveB: 'B'
};
const objetoC = new Object();
objetoC.chaveC = 'C';

Object.setPrototypeOf(objetoB, objetoA);
Object.setPrototypeOf(objetoC, objetoB)
console.log(objetoC.chaveB);
console.log(Object.getPrototypeOf(objetoC));*/

function Produto(nome, preço) {
    this.nome = nome;
    this.preço = preço;
};

Produto.prototype.desconto = function(percentual) {
  this.preço = this.preço - (this.preço * (percentual / 100));
};

Produto.prototype.aumento = function(percentual) {
    this.preço = this.preço + (this.preço * (percentual / 100))
}

const p1 = new Produto('Camiseta', 50);
const p2 = {
    nome: 'Caneca',
    preço: 15
};
const p3 = Object.create(Produto.prototype);
p3.preço = 10;

Object.setPrototypeOf(p2, Produto.prototype);

p1.aumento(50);
p2.desconto(10);
p3.aumento(20);

console.log(p1);
console.log(p2);
console.log(p3);