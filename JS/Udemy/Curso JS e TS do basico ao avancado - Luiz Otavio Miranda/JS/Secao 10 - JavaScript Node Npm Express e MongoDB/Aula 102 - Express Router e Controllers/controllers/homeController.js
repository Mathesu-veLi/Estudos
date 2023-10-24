exports.páginaInicial = (req, res) => {
    res.send(`
        <form method="POST">
            Nome: <input type="text" name="name">
            <button>Enviar formulário</button>
        </form>
    `);
}

exports.trataPost = (req, res) => {
    res.send('Ei, sou sua nova rota de POST');
}