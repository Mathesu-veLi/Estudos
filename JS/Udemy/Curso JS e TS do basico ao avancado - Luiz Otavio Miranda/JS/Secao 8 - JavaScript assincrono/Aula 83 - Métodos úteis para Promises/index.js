function rand(max, min) {
    min *= 1000;
    max *= 1000;
    return Math.floor(Math.random() * (max - min) + min);
};

function esperaAi(msg, tempo) {
    return new Promise((resolve, reject) => {
        if (typeof msg !== 'string') {
            reject(new Error('BAD value'));
            return;
        };
        setTimeout(() => {
            resolve(msg.toUpperCase() + ' - Passei');
        }, tempo);
    });
};

function baixaPágina() {
    const emCache = true;

    if(emCache) {
        return Promise.reject('Página em cache')
    } else {
        return esperaAi('Baixei a página', 3000)
    }
};

baixaPágina().then(dadosPágina => {
    console.log(dadosPágina)
}).catch(e => console.log('ERRO:', e))