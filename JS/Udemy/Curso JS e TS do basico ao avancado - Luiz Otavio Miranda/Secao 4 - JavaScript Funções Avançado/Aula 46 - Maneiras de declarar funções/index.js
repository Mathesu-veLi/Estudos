// Quando criamos uma função usando function, podemos executa-la em qualquer lugar do código, até mesmo antes dela

falaOi()

function falaOi() {
    console.log('oi');
};

// Podemos usar funções como dado de uma variável (function expression)

const souUmDado = function nomeDaFunção() {
    console.log('Sou um dado');
};

// Funções podem executar outras funções, até mesmo se ela for um parâmetro

function executaFunção(função) {
    console.log('Vou executar sua função abaixo')
    função();
}

executaFunção(souUmDado);

const funçãoArrow = () => {
    console.log('Sou uma arrow function');
};

funçãoArrow();

//Podemos colocar funções em um objeto

const obj = {
    falar() {
        console.log('Estou falando');
    }
};

obj.falar();