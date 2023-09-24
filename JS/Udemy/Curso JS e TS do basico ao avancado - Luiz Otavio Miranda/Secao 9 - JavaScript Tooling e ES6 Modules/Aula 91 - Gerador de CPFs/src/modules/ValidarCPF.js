export default class ValidarCPF {
    constructor(cpf) {
        Object.defineProperty(this, 'cpfFormatado', {
            get: function () {
                cpf = String(cpf);
                return cpf.replace(/\D+/g, '');
            },
            enumerable: true
        });
    };

    valida() {
        if (typeof this.cpfFormatado === 'undefined' || this.cpfFormatado.length !== 9) return false;
        this.cpfArray = Array.from(this.cpfFormatado);
        if (this.cpfFormatado[0].repeat(this.cpfFormatado.length) === this.cpfFormatado) return false;

        this.descobreDígito(this.cpfArray, 10);
        this.descobreDígito(this.cpfArray, 11);
        return this.cpfArray.join('');
    };

    descobreDígito(array, valor) {
        let total = 0;
        array.reduce((acumulador, elemento) => {
            total += Number(elemento) * acumulador;
            return acumulador -= 1;
        }, valor);
        let dígito = 11 - (total % 11);
        array.push(dígito > 9 ? 0 : dígito);
        return dígito;
    };
};