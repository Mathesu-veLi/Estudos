function IMC() {
    let formulário = document.querySelector('form');
    let resultado = document.querySelector('#resultado');

    formulário.addEventListener('submit', (e) => {
        e.preventDefault();
        let imc = calcularIMC();
        escreverIMCNaPágina(imc);
    });

    function calcularIMC() {
        let peso = Number(document.querySelector('#input-peso').value);
        let altura = Number(document.querySelector('#input-altura').value);

        if (!peso || !altura) {
            return validarDados(peso, altura);
        } else {
            let imc = peso / Math.pow(altura, 2);
            return imc.toFixed(2);
        }
        
    }

    function validarDados(peso, altura) {
        if (!peso) {
            return 'Peso inválido';
        } else if (!altura) {
            return 'Altura inválida';
        }
    }

    function escreverIMCNaPágina(imc) {
        if (imc == 'Peso inválido' || imc == 'Altura inválida') {
            resultado.innerHTML = imc;
        } else {
            resultado.innerHTML = `<mark>Seu IMC é ${imc}, logo, sua situação é ${calcularSituação(imc)}</mark>`;
        }
            
    }

    function calcularSituação(imc) {
        if (imc < 18.5) {
            return 'Abaixo do peso';
        } else if (imc >= 18.5 && imc <= 24.9) {
            return 'Peso normal';
        } else if (imc >= 25 && imc <= 29.9) {
            return 'Sobrepeso';
        } else if (imc >= 30 && imc <= 34.9) {
            return 'Obesidade grau 1';
        } else if (imc >= 35 && imc <= 39.9) {
            return 'Obesidade grau 2';
        } else{
            return 'Obesidade grau 3';
        }
    }
}

IMC();