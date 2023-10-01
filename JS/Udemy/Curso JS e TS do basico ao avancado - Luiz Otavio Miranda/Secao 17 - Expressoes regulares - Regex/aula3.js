/*
  Quantificadores:
    * - 0 ou mais (opcional)
    + - 1 ou mais (obrigatório)
    ? - 0 ou 1 (opcional)
    \ Caractere de escape
*/

const { texto, arquivos } = require('./base');

const regExp1 = /Jo+ão+/gi;

console.log(texto);
console.log(texto.match(regExp1));

const regExp2 = /\.(jpe?g)/gi;

for (const arquivo of arquivos) {
  const válido = arquivo.match(regExp2);

  if(!válido) continue;

  console.log('');
  console.log(arquivo, arquivo.match(regExp2));
}
