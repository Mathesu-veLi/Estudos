function* geradora1() {
    yield 'Valor 1';
    yield 'Valor 2';
    yield 'Valor 3';
};

function* geradora2() {
    let i = 0;
    
    while(true) {
        yield i;
        i++;
    };
};

const g2 = geradora2();

for (let c = 0; c <= 10; c++){
    console.log(g2.next().value);
};

function* geradora3() {
    yield 0;
    yield 1;
    yield 2;
};

function* geradora4() {
    yield* geradora3();
    yield 3;
    yield 4;
    yield 5;
};

const g4 = geradora4();

for(let valor of g4) {
    console.log(valor);
};

function* geradora5() {
    yield function () {
        console.log('Olá1');
    };

    return function() {
        console.log('Olá retornado')
    }

    yield function() {
        console.log('Olá2')
    };
};

const g5 = geradora5();
const func1 = g5.next().value;
const func2 = g5.next().value;


func1();
func2();