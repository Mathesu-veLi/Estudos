const somar = (x, y) => {
    if (typeof x !== 'number' || typeof y !== 'number') {
        throw new ReferenceError('x e y precisam ser números')
    }

    return x + y;
}

try {
    console.log(somar(2, 4));
    console.log(somar(2, '4'));
} catch(e) {
    console.log(e)
}