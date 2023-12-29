enum Cores {
    VERMELHO = 10, // 10
    VERDE = 100, // 100
    AZUL = 200, // 200
}

enum Cores {
    ROXO = 'ROXO',
    AMARELO = 201,
    ROSA,
}

function escolhaACor(cor: Cores): void {
    console.log(Cores[cor]);
}
