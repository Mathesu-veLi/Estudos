const pessoa1 = {
    nome: 'Matheus',
    sobrenome: 'Silva',
    idade: 13,

    fala(){
        console.log(`A idade atual de ${this.nome} ${this.sobrenome} é ${this.idade}`);
    },

    incrementarIdade(){
        this.idade++
    }
};

pessoa1.fala();
pessoa1.incrementarIdade();
pessoa1.fala();