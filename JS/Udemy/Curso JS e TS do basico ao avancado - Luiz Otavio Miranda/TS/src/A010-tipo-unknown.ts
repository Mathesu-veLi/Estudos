let x: unknown;
x = 100;
x = 'Luiz';
x = 900;
x = '10';
const y = 100;

if (typeof x !== 'number') throw new Error('x must be a number');
console.log(x + y)
