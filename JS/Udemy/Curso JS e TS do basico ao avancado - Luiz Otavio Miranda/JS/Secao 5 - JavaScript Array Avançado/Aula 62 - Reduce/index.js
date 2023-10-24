const números = [5, 50, 80, 1, 2, 3, 5, 8, 7, 11, 15, 22, 27];
const total = números.reduce((acumulador, valor) => {
    acumulador.push(valor * 2);
    return acumulador;
}, []);

console.log(total);

const pessoas = [
    {nome: 'Maria', idade: 23},
    {nome: 'Luiz', idade: 62},
    {nome: 'Eduardo', idade: 55},
    {nome: 'Letícia', idade: 19 },
    {nome: 'Wallace', idade: 47},
    {nome: 'Rosana', idade: 32},
];


const maisVelha = pessoas.reduce((acumulador, valor) => {
    if (acumulador.idade > valor.idade) {
        return acumulador;
    }

    return valor;
})

console.log(maisVelha);