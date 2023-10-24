const rand = (min, max) => Math.floor(Math.random() * (max - min) + min);

const geraMaiúscula = () => String.fromCharCode(rand(65, 91));
const geraMinuscula = () => String.fromCharCode(rand(97, 123));
const geraNúmeros = () => String.fromCharCode(rand(48, 58));
const símbolos = '!@#$%&*-_=+-*|';
const geraSímbolo = () => símbolos[rand(0, 5)];

export default function geraSenha(qtd, maiúsculas, minusculas, números, símbolos) {
    const senhaArray = [];
    qtd = Number(qtd);

    for(let i = 0; i < qtd; i++) {
        maiúsculas && senhaArray.push(geraMaiúscula());
        minusculas && senhaArray.push(geraMinuscula());
        números && senhaArray.push(geraNúmeros());
        símbolos && senhaArray.push(geraSímbolo());
    };
    
    return senhaArray.join('').slice(0, qtd);
};