const números = [5, 50, 80, 1, 2, 3, 5, 8, 7, 11, 15, 22, 27];
const númerosFiltrados = números.filter((valor, índice) => {
    console.log(`O valor da vez é o ${valor} de índice ${índice}`);
    return valor > 10;
});
console.log(númerosFiltrados);

/*let númerosMaioresQue10 = Array();
for (let c of números) {
    if (c > 10) {
        númerosMaioresQue10.push(c);
    };
};
console.log(númerosMaioresQue10);*/


const pessoas = [
    {nome: 'Luiz', idade: 62},
    {nome: 'Maria', idade: 23},
    {nome: 'Eduardo', idade: 55},
    {nome: 'Letícia', idade:19 },
    {nome: 'Rosana', idade: 32},
    {nome: 'Wallace', idade: 47}
];

const pessoasComNomeGrande = pessoas.filter(valor => valor.nome.length >= 5);
const pessoasMaioresDe50Anos = pessoas.filter(valor => valor.idade >= 50);
const nomesQueTerminamComA = pessoas.filter(valor => valor.nome.toLowerCase().endsWith('a'));
console.log(pessoasComNomeGrande);
console.log(pessoasMaioresDe50Anos);
console.log(nomesQueTerminamComA);