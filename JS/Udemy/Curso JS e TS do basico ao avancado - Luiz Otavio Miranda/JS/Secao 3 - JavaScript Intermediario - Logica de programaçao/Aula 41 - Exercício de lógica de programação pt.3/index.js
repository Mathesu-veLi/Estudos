const verificarSeÉNúmero = (x) => x % 1 === 0 ? identificarDivisores(x) : 'Não é um número';

const identificarDivisores = (x) => {
    if (x % 5 === 0 & x % 3 === 0) return 'FizzBuzz';
    if (x % 5 === 0) return 'Buzz';
    if (x % 3 === 0) return 'Fizz';
    return x;
}

for (let i = 0; i <= 100; i++) {
    console.log(i, verificarSeÉNúmero(i));
}
