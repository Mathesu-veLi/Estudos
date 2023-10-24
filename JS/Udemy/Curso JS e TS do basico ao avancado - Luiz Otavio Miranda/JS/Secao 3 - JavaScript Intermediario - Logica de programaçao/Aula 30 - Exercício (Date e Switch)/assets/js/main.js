const hora = document.querySelector('.content h1');
const diaAtual = {
    objetoDate: new Date(),
    calcularDiaDaSemana() {
        let diaDaSemana = this.objetoDate.getDay();
        /*switch(diaDaSemana) {
            case 0: 
                diaDaSemana = 'Domingo';
                break;
            case 1: 
                diaDaSemana = 'Segunda-feira';
                break;
            case 2: 
                diaDaSemana = 'Terça-feira';
                break;
            case 3: 
                diaDaSemana = 'Quarta-feira';
                break;
            case 4: 
                diaDaSemana = 'Quinta-feira';
                break;
            case 5: 
                diaDaSemana = 'Sexta-feira';
                break;
            case 6: 
                diaDaSemana = 'Sábado';
                break;
            default: 
                diaDaSemana = 'Date Error!';
                break;
        }
        return diaDaSemana;*/

        dias = ['domingo', 'segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado'];
        return dias[diaDaSemana];
    },
    calcularMês() {
        let mêsAtual = this.objetoDate.getMonth();
        /*switch (mêsAtual) {
            case 0: 
                mêsAtual = 'janeiro';
                break;
            case 1: 
                mêsAtual = 'fevereiro';
                break;
            case 2: 
                mêsAtual = 'março';
                break;
            case 3: 
                mêsAtual = 'abril';
                break;
            case 4: 
                mêsAtual = 'maio';
                break;
            case 5: 
                mêsAtual = 'junho';
                break;
            case 6: 
                mêsAtual = 'julho';
                break;
            case 7: 
                mêsAtual = 'agosto';
                break;
            case 8: 
                mêsAtual = 'setembro';
                break;
            case 9: 
                mêsAtual = 'outubro';
                break;
            case 10: 
                mêsAtual = 'novembro';
                break;
            case 11: 
                mêsAtual = 'dezembro';
                break;
        }
        return mêsAtual;*/
        
        meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'];
        return meses[mêsAtual];
    },
    concertarZero(número) {
        return número >= 10 ? número : `0${número}`;
    }
};



hora.innerHTML = `${diaAtual.calcularDiaDaSemana()}, ${diaAtual.objetoDate.getDate()} de ${diaAtual.calcularMês()} de ${diaAtual.objetoDate.getFullYear()} <br>${diaAtual.concertarZero(diaAtual.objetoDate.getHours())}:${diaAtual.concertarZero(diaAtual.objetoDate.getMinutes())}`;


/*const data = new Date();
hora.innerHTML = `${data.toLocaleDateString('pt-BR', { dateStyle: 'full'})} <br>${data.toLocaleTimeString("pt-BR", { hour12: false, hour: "2-digit", minute: "2-digit" })}`;*/
