function Calculadora() {
    this.display = document.querySelector('.display'),
        this.clearBtn = document.querySelector('.btn-clear'),

        this.start = () => {
            this.buttonsClick();
            this.pressEnter();
            this.preventingLetterTyping();
        },

        this.buttonsClick = () => {
            document.addEventListener('click', (e) => {
                const element = e.target;
                if (element.classList.contains('btn-num')) {
                    this.btnStopDisplay(element.innerText);
                    this.display.focus()
                };

                if (element.classList.contains('btn-clear')) {
                    this.clearDisplay();
                };

                if (element.classList.contains('btn-del')) {
                    this.deleteOne();
                };

                if (element.classList.contains('btn-eq')) {
                    this.performCalculation();
                };
            });
        },

        this.clearDisplay = () => {
            this.display.value = '';
        },

        this.deleteOne = () => {
            this.display.value = this.display.value.slice(0, -1);
        },

        this.pressEnter = () => {
            this.display.addEventListener('keyup', e => {
                if (e.keyCode === 13) {
                    this.performCalculation();
                }
            })
        },

        this.performCalculation = () => {
            let calculation = this.display.value;

            try {
                calculation = eval(calculation);
                if (!calculation && calculation === '0') {
                    alert('Conta inválida')
                    return;
                }

                this.display.value = calculation;
            } catch (e) {
                alert('Conta invalida');
                return;
            }
        },


        this.btnStopDisplay = (valor) => {
            this.display.value += valor;
        },

        this.preventingLetterTyping = () => {
            this.display.addEventListener('keypress', e => {
                if (e.key.toLowerCase() != e.key.toUpperCase() && e.key !== 'Enter') {
                    setTimeout(() => {
                        this.deleteOne();
                    }, 1);
                }
            })
        }
}

const calc = new Calculadora();
calc.start();