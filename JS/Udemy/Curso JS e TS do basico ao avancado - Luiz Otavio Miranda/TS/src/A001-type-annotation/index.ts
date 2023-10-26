// Types

let personName: string = 'Luiz';
let age: number = 30;
let adult: boolean = true;
let symbol: symbol = Symbol('qualquer-symbol');
// let big: bigint = 10n;

// Arrays

let numberArray: Array<number> = [1, 2, 3];
let numberArray2: number[] = [1, 2, 3];

let stringArray: Array<string> = ['1', '2', '3'];
let stringArray2: string[] = ['1', '2', '3'];

// Objects

let person: { name: string; age: number; adult?: boolean } = {
    name: 'Matheus',
    age: 13,
    adult: false,
};

// Functions

function sum(x: number, y: number): number {
    return x + y;
}

const sum2: (x: number, y: number) => number = (x, y) => x + y;
