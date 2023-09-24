let númeroParaAnalisar = Number(prompt('Digite um número'));

let número = document.querySelector("#numero");
número.innerHTML = númeroParaAnalisar;

let raizQuadrada = (númeroParaAnalisar ** 0.5).toFixed(2);
document.querySelector("#raiz-quadrada").innerHTML = raizQuadrada;

let éInteiro = Number.isInteger(númeroParaAnalisar);
document.querySelector("#inteiro").innerHTML = éInteiro;

let éNaN = Number.isNaN(númeroParaAnalisar);
document.querySelector("#NaN").innerHTML = éNaN;

let númeroArredondadoParaBaixo = Math.floor(númeroParaAnalisar);
document.querySelector("#arredondado-para-baixo").innerHTML = númeroArredondadoParaBaixo;

let númeroArredondadoParaCima = Math.ceil(númeroParaAnalisar);
document.querySelector("#arredondado-para-cima").innerHTML = númeroArredondadoParaCima;

let númeroCom2CasasDecimais = númeroParaAnalisar.toFixed(2);
document.querySelector("#com-duas-casas").innerHTML = númeroCom2CasasDecimais;