/*
    Falsy:
        false
        0
        '' "" ``
        null / undefined
        NaN
*/

/*
console.log('Luiz' && 0 && 'Maria') // 0 -> pois 0 é um valor Falsy
console.log('Luiz' && 'Maria') // 'Maria' -> pois Maria é o último valor positivo encontrado (strings não vazias são consideradas true)
*/

function falaOi() {
    return 'Oi';
}

let vaiExecutar = false;
console.log(vaiExecutar && falaOi()); // false
console.log(!vaiExecutar && falaOi()); //Oi

console.log(0 || false || null || 'Matheus Levi' || true); // 'Matheus Levi' -> pois Matheus Levi é o primeiro valor positivo encontrado (strings não vazias são consideradas true)
/*
const corUsuario = 'vermelho';
const corPadrão = corUsuario || 'preto'; // vermelho
*/

const corUsuario = null;
const corPadrão = corUsuario || 'preto'; // preto

console.log(corPadrão)

const a = 0;
const b = null;
const c = 'false';
const d = false;
const e = NaN;

console.log(a || b || c || d || e) // false (const c)