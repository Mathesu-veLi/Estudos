/*
Primitivos (imutáveis) - string, number, boolean, undefined, null (bigint, symbol) - Valores copiados

Referência (mutável) - array, object, function - Passados por referência 
*/

/*let a = 5
let b = a // Cópia

let c = [1, 2, 3];
let d = c; // Referência
let e = d;
let f = [...e]; //Cópia
console.log(a, b);

c.push(4);
console.log(a, b);

d.pop();
console.log(a, b);

c.push('Luiz');
console.log(c);*/

const pessoa = {
    nome: 'Luiz',
    sobrenome: 'Otávio'
};


// const b = pessoa; // Referência
const b = {...a}; // Cópia

pessoa.nome = 'João';
console.log(a);
console.log(b);