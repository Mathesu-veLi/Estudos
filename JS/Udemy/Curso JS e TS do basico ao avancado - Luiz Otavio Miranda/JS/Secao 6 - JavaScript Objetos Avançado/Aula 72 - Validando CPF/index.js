function ValidarCPF(cpf) {
    Object.defineProperty(this, 'cpfFormatado', {
        get: function() {
            cpf = String(cpf);
            return cpf.replace(/\D+/g, '');
        },
        enumerable: true
    });
};

ValidarCPF.prototype.valida = function() {
    if(typeof this.cpfFormatado === 'undefined' || this.cpfFormatado.length !== 11) return false;
    this.cpfArray = Array.from(this.cpfFormatado.slice(0, -2));
    if(this.cpfFormatado[0].repeat(this.cpfFormatado.length) === this.cpfFormatado) return false;

    this.descobreDígito(this.cpfArray, 10);
    this.descobreDígito(this.cpfArray, 11);
    if(String(this.cpfArray.join('')) !== String(this.cpfFormatado)) return false;
    return true;
}

ValidarCPF.prototype.descobreDígito = (array, valor) => {
    let total = 0;
    array.reduce((acumulador, elemento) => {
        total += elemento * acumulador;
        return acumulador -= 1;
    }, valor);
    let dígito = 11 - (total % 11);
    array.push(dígito > 9 ? 0 : dígito);
};


const cpf = new ValidarCPF('111.111.111-11');
if(cpf.valida()) {
    console.log('CPF válido');
} else {
    console.log('CPF inválido')
}