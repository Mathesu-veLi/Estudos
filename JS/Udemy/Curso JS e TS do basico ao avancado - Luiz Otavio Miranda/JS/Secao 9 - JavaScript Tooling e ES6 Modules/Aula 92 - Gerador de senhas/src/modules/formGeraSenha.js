import geraSenha from "./geradores";

const senhaGerada = document.querySelector('.senha-gerada');
const quantidadeDeCaracteres = document.querySelector('#qnt').value;
const checkMaiúsculas = document.querySelector('#maiusculas');
const checkMinusculas = document.querySelector('#minusculas');
const checkNúmeros = document.querySelector('#num');
const checkSímbolos = document.querySelector('#símbolos');
const gerarSenhaBtn = document.querySelector('#gerar');

export default () => {
    gerarSenhaBtn.addEventListener('click', () => {
        senhaGerada.innerHTML = geraSenha(quantidadeDeCaracteres, 
            checkMaiúsculas.checked, 
            checkMinusculas.checked, 
            checkNúmeros.checked, 
            checkSímbolos.checked) || 'Nada selecionado';
    });
};