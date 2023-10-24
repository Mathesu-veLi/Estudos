/*let data;
// data = new Date(2019, 3, 15, 14, 20, 09); // ano, mês, dia, hora, minutos, segundos, milissegundos
data = new Date(Date.now());
console.log('Dia', data.getDate());
console.log('Mês', data.getMonth());
console.log('Ano', data.getFullYear());
console.log('Hora', data.getHours());
console.log('Min', data.getMinutes());
console.log('Seg', data.getSeconds());
console.log('ms', data.getMilliseconds());
console.log('Dia da Semana', data.getDay()); // 0 - Domingo, 6 - Sábado
console.log(data.toString()); */

function formatarData(data)
{
    const dia = concertarZero(data.getDate());
    const mês = concertarZero(data.getMonth());
    const ano = concertarZero(data.getFullYear());
    const hora = concertarZero(data.getHours());
    const minutos = concertarZero(data.getMinutes());
    const segundos = concertarZero(data.getSeconds());
    return `${dia}/${mês}/${ano} ${hora}:${minutos}:${segundos}`;
}

function concertarZero(número)
{
    return número >= 10 ? número : `0${número}`;
}

const data = new Date();
const dataBrasil = formatarData(data);
console.log(dataBrasil)