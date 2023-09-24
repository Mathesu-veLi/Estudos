function Produto(nome, preço) {
    this.nome = nome;
    this.preço = preço;
};
Produto.prototype.aumento = function(quantia) {
    this.preço += quantia;
};
Produto.prototype.desconto = function(quantia) {
    this.preço -= quantia;
};

function Camiseta(nome, preço, cor) {
    Produto.call(this, nome, preço);
    this.cor = cor;
};
Camiseta.prototype = Object.create(Produto.prototype);
Camiseta.prototype.constructor = Camiseta;

Camiseta.prototype.aumento = function(percentual) {
    this.preço = this.preço + (this.preço * (percentual / 100));
};

function Caneca(nome, preço, material, estoque) {
    Produto.call(this, nome, preço);
    this.material = material;
    this.estoque = estoque;

    Object.defineProperty(this, 'estoque', {
        enumerable: true,
        configurable: false,
        get: function() {
            return estoque;
        },
        set: function(valor) {
            if (typeof valor !== 'number') return;
            estoque = valor;
        }
    })
};
Caneca.prototype = Object.create(Produto.prototype);
Caneca.prototype.constructor = Caneca;

const produto = new Produto('Gen', 111);
const camiseta = new Camiseta('Regata', 7.5, 'Preta');
const caneca = new Caneca('Caneca', 11, 'Porcelana', 5);

camiseta.aumento(10);
produto.aumento(10);

console.log(camiseta);
console.log(produto);
console.log(caneca);