let x;
if (typeof x === 'undefined') x = 20;
console.log(x * 2);

export function createPerson(
    firstName: string,
    lastName?: string,
): {
    firstName: string;
    lastName?: string;
} {
    return {
        firstName,
        lastName,
    };
}

export function squareOf(x: any) {
    if (typeof x !== 'number') return null;
    return x * x;
}

const squareOfTwoNumber = squareOf(2);
const squareOfTwoString = squareOf('2');

if (typeof squareOfTwoNumber !== 'number') {
    throw TypeError('Value must be a number');
}

console.log(squareOfTwoNumber * 100);
