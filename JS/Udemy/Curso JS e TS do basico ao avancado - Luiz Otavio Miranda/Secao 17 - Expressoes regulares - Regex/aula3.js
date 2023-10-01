/*
  Quantificadores:
    * - 0 ou mais {0, } (opcional)
    + - 1 ou mais {1, } (obrigatório)
    ? - 0 ou 1 {0, 1} (opcional)
    \ Caractere de escape
    {mínimo, máximo} ( 
      {10,} no mínimo 10
      {,10} de 0 a 10
    )
*/

const { texto, arquivos } = require('./base');

const regExp1 = /Jo+ão+/gi;

console.log(texto);
console.log(texto.match(regExp1));

const regExp2 = /\.(jpe{0,}g)/gi;

for (const arquivo of arquivos) {
  const válido = arquivo.match(regExp2);

  if(!válido) continue;

  console.log('');
  console.log(arquivo, arquivo.match(regExp2));
}
