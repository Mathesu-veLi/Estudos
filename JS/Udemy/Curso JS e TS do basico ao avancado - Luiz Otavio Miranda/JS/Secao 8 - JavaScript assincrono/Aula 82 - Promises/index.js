function rand(max, min) {
    min *= 1000;
    max *= 1000;
    return Math.floor(Math.random() * (max - min) + min);
}

function esperaAi(msg, tempo) {
    return new Promise((resolve, reject) => {
        if(typeof msg !== 'string') {
            reject(new Error('BAD value'))
        }
        setTimeout(() => {
            resolve(msg);
        }, tempo);
    });
};

esperaAi('Conexão com o BD...', rand(1, 3)).then(resposta => {
    console.log(resposta);
    return esperaAi('Buscando dados da Base...', rand(1, 3));
}).then(resposta => {
    console.log(resposta);
    return esperaAi(2, rand(1, 3));
}).then(resposta => {
    console.log(resposta);
}).then(resposta => {
    console.log('Exibe dados na tela');
}).catch(e => {
    console.log('Erro:', e);
});

console.log('Isso será exibido antes de qualquer promise')