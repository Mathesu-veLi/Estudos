const objectA: { readonly keyA: string; keyB: string; [key: string]: unknown } = {
    keyA: 'Valor A',
    keyB: 'Valor B',
};

// objectA.keyA = 'Value';
objectA.keyC = 'Other value';
objectA.keyD = 'Other Other value';

console.log(objectA);
