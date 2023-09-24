// funções declaradas com function tem a variável arguments, que sustenta todos os argumentos dados, mesmo os não necessários

function somarNúmeros(a, b, c) {
    total = 0;
    for (let número of arguments) {
        total += número;
    }
    return `${total} ${a}, ${b}, ${c}`;
}
console.log(somarNúmeros(1, 2, 3, 4, 5, 6, 7));


// quando não são dados argumentos suficientes, eles são declarados como undefined

function somarNúmeros2(a, b, c, d, e, f) {
    console.log(a, b, c, d, e, f);
}
somarNúmeros2(1, 2, 3);


// podemos usar parâmetros opcionais para caso não seja dado argumento

function somarNúmeros3(a, b = 2, c = 4) {
    console.log(a + b + c);
}
somarNúmeros3(2, undefined, 10);


// podemos usar arrays ou objetos como parâmetro

function mostrarNome([nome, sobrenome]) {
    console.log(nome, sobrenome);
}
mostrarNome(['Matheus Levi', 'Fernandes da Silva']);


// o restOperator (...) faz com que o parâmetro receba todos os argumentos que sobraram (sempre deve ser o último)

function conta(operador, acumulador, ...números) {
    for (let número of números) {
        if (operador === '+') acumulador += número;
        if (operador === '-') acumulador -= número;
        if (operador === '*') acumulador *= número;
        if (operador === '/') acumulador /= número;
    }
}
conta('+', 0, 20, 30, 40, 50);