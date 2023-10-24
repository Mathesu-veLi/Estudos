
function criaPessoa(nome, sobrenome, altura, peso) {
    return {
        nome,
        sobrenome,

        //Constructor function 
        get nomeCompleto(){
            return `${this.nome} ${this.sobrenome}` 
        },

        //Setter
        set nomeCompleto(valor) {
            valor = valor.split(' ');
            this.nome = valor.shift();
            this.sobrenome = valor.join(' ');
        },

        altura,
        peso,
        //Factory function
        /*imc() {
            const índice = this.peso / (this.altura**2);
            return índice.toFixed(2);
        }*/

        //Constructor function
        get imc() {
            const índice = this.peso / (this.altura**2);
            return índice.toFixed(2);
        }
    };
};

const p1 = criaPessoa('Matheus', 'Silva', 1.54, 51);
console.log(p1.nomeCompleto)
p1.nomeCompleto = 'Luiz Fernandes da Silva'
console.log(p1.nomeCompleto)