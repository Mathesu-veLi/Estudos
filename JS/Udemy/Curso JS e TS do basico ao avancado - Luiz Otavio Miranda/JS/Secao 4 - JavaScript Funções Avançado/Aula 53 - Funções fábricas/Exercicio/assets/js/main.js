const criarCalculadora = () => {
    return {
        display: document.querySelector('.display'),
        clearBtn: document.querySelector('.btn-clear'),

        start() {
            this.buttonsClick();
            this.pressEnter();
            this.preventingLetterTyping();
        },

        buttonsClick() {
            document.addEventListener('click', (e) => {
                const element = e.target;
                if (element.classList.contains('btn-num')) {
                    this.btnStopDisplay(element.innerText);
                };

                if (element.classList.contains('btn-clear')) {
                    this.clearDisplay()
                };

                if (element.classList.contains('btn-del')) {
                    this.deleteOne();
                };

                if (element.classList.contains('btn-eq')) {
                    this.performCalculation();
                };
            });
        },

        clearDisplay() {
            this.display.value = '';
        },

        deleteOne() {
            this.display.value = this.display.value.slice(0, -1);
        },

        pressEnter() {
            this.display.addEventListener('keyup', e => {
                if (e.keyCode === 13) {
                    this.performCalculation();
                }
            })
        },

        performCalculation() {
            let calculation = this.display.value;

            try {
                calculation = eval(calculation);

                if (!calculation) {
                    alert('Conta inválida')
                    return;
                }

                this.display.value = calculation;
            } catch (e) {
                alert('Conta invalida');
                return;
            }
        },


        btnStopDisplay(valor) {
            this.display.value += valor;
        },

        preventingLetterTyping() {
            this.display.addEventListener('keypress', e => {
                if (e.key.toLowerCase() != e.key.toUpperCase()) {
                    setTimeout(() => {
                        this.deleteOne();
                    }, 1);
                }
            })
        }
    }
};

const calc = criarCalculadora();

calc.start();