const express = require('express');
const app = express();

app.use(express.urlencoded({extended: true}))

app.get('/', (req, res) => {
    res.send(`
        <form method="POST">
            Nome: <input type="text" name="name">
            <button>Enviar formulário</button>
        </form>
    `);
});

app.get('/teste/:idUsuarios?', (req, res) => {
    console.log(req.params)
    console.log(req.query)
    res.send(req.params.idUsuarios)
})

app.post('/', (req, res) => {
    console.log(req.body)
    res.send(`O que você me enviou foi : ${req.body.name}`)
})

app.listen(3000, () => {
    console.log('Acessar http://localhost:3000');
    console.log('Servidor executando na porta 3000');
});
