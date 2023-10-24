const data = new Date("1987-04-26 00:00:00");
const diaDaSemana = calcularDiaDaSemana()

function calcularDiaDaSemana(){
    let diaDaSemana = data.getDay();
    switch (diaDaSemana)
    {
        case 0:
            diaDaSemana = 'Domingo';
            break
        case 1:
            diaDaSemana = 'Segunda';
            break
        case 2:
            diaDaSemana = 'Terça';
            break
        case 3:
            diaDaSemana = 'Quarta';
            break
        case 4:
            diaDaSemana = 'Quinta';
            break
        case 5:
            diaDaSemana = 'Sexta';
            break
        case 6:
            diaDaSemana = 'Sábado';
            break
    }
    return diaDaSemana;
}

console.log(diaDaSemana);