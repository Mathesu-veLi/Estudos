const elementos = [
    {tag: 'p', text: 'Frase 1'},
    {tag: 'div', text: 'Frase 2'},
    {tag: 'footer', text: 'Frase 3'},
    {tag: 'section', text: 'Frase 4'}
];

var div = document.querySelector('.content');

for(let c = 0; c <= elementos.length; c++) {
    criarElemento(elementos[c].tag, elementos[c].text);
}

function criarElemento(tag, text)
{
    let obj = document.createElement(tag);
    obj.innerText = text;
    div.appendChild(obj);
}