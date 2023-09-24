function Produto(nome, preço, estoque) {
    Object.defineProperty(this, 'estoque', {
        enumerable: true,
        value: estoque,
        writable: true,
        configurable: true,
    });

    Object.defineProperties(this, {
        nome: {
            enumerable: true,
            value: nome,
            writable: false,
            configurable: false
        },

        preço: {
            enumerable: true,
            value: preço,
            writable: true,
            configurable: false
        }
    });
}

const p1 = new Produto('Camiseta', 20, 3);
console.log(p1);