import ValidarCPF from "./ValidarCPF";

export default class GerarCPF {
    constructor() {

    };

    rand(min = 100000000, max = 999999999) {
        return String(Math.floor(Math.random() * (max - min) + min));
    };

    formatar(cpf) {
        return (
            cpf.slice(0, 3) + '.' +
            cpf.slice(3, 6) + '.' +
            cpf.slice(6, 9) + '-' +
            cpf.slice(9, 11)
        );
    };

    geraNovoCpf() {
        const cpfSemDígito = this.rand();
        const novoCpf = new ValidarCPF(cpfSemDígito);
        return this.formatar(novoCpf.valida());
    };
};