import GerarCPF from './modules/GerarCPF';
import './assets/css/style.css';

(function() {
    const gera = new GerarCPF();
    const cpfGerado = document.querySelector('.cpf-gerado');
    cpfGerado.innerHTML = gera.geraNovoCpf();
})();