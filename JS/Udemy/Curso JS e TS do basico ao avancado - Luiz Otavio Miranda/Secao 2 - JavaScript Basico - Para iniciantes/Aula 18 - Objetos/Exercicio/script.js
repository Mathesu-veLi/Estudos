function meuEscopo() {
    const pessoasRegistradas = Array();
    const pessoas = document.querySelector('#ipessoas');
    const form = document.querySelector('.form');

    form.addEventListener('submit', (evento) => {
        evento.preventDefault();
        adicionarPessoa();
    })


    function adicionarPessoa() {
        const nome = document.querySelector('#inome').value;
        const sobrenome = document.querySelector('#isobrenome').value;
        const peso = document.querySelector('#ipeso').value;
        const altura = document.querySelector('#ialtura').value;
        pessoasRegistradas.push({
            nome,
            sobrenome,
            peso,
            altura
        });
        pessoas.innerHTML += `${nome} ${sobrenome} ${peso} ${altura} <br>`;
        console.log(pessoasRegistradas);
    }
}

meuEscopo();