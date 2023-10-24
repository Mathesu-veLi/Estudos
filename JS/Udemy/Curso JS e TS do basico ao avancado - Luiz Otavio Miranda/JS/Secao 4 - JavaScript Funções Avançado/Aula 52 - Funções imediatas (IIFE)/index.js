// IIFE -> Immediately invoked function expression

(function(idade, peso, altura) {
    const sobrenome = 'Silva';
    function criaNome(nome) {
        return nome + ' ' + sobrenome;
    }

    function falaNome() {
        console.log(criaNome('Matheus'));
    }

    falaNome();
    console.log(idade, peso, altura)
})(13, 51, 1.54);

