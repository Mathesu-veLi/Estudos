function retornaFunção() {
    const nome = 'Matheus';
    return function() {
        return nome;
    };
};

const função = retornaFunção();
console.log(função);