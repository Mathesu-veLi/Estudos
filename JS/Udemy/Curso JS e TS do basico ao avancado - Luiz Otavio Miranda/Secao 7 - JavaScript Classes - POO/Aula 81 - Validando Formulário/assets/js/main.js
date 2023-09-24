class Usuário {
    constructor() {
        this.nome = document.querySelector('#nome').value;
        this.sobrenome = document.querySelector('#sobrenome').value;
        this.cpf = document.querySelector('#cpf').value;
        this.user = document.querySelector('#user').value;
        this.senha = document.querySelector('#senha').value;
        this.repetirSenha = document.querySelector('#re-senha').value;
        this.mensagemFinal = document.querySelector('#mensagemFinal');
    };

    validar() {
        if (this.verificarSeÉVazio() !== true) return this.verificarSeÉVazio();

        if (!this.validarCPF(this.cpf)) return 'CPF inválido!';

        if (this.validarUser() !== true) return this.validarUser();

        if (this.senha !== this.repetirSenha) return 'As senhas não conferem!'

        if (this.validarSenha() !== true) return this.validarSenha();

        return true;
    };

    verificarSeÉVazio() {
        if (!this.nome) return 'Nome vazio';
        if (!this.sobrenome) return 'Sobrenome vazio';
        if (!this.cpf) return 'CPF vazio';
        if (!this.user) return 'Nome de Usuário vazio';
        if (!this.senha) return 'Senha vazio';
        if (!this.repetirSenha) return 'Repetir senha vazio';

        return true;
    };

    validarUser() {
        let expressãoRegular = /^[a-zA-Z0-9]+$/;
        if (!expressãoRegular.test(this.user)) return 'Usuário precisa conter apenas letras e números';

        if (this.user.length < 3 || this.user.length > 12) return 'Usuário precisa conter mais de 3 caracteres e menos de 12';

        return true;
    };

    validarSenha() {
        if (this.senha.length < 6 || this.senha.length > 12) return 'A senha precisa conter entre 6 e 12 caracteres';

        return true;
    };

    validarCPF(cpfEnviado) {
        const cpf = new ValidarCPF(cpfEnviado);
        if (!cpf.valida()) {
            return false;
        };
        return true;
    };
};

function cadastrar() {
    const usuário = new Usuário();
    if(usuário.validar() !== true) {
        this.mensagemFinal.innerHTML = `Impossível cadastrar! ${usuário.validar()}`;
        return;
    };
    alert(`Usuário ${usuário.nome} cadastrado com sucesso!`);
    document.querySelector('form').submit();
};

