// {condição} ? 'Valor para verdadeiro' : 'Valor para falso'
// {condição} || 'Valor para falso'

const pontuaçãoUsuário = 100;
const nívelUsuário = pontuaçãoUsuário >= 1000 ? 'Usuário VIP' : 'Usuário normal';

const corUsuário = null;
const corPadrão = corUsuário || 'Preta';

console.log(nívelUsuário, corPadrão);