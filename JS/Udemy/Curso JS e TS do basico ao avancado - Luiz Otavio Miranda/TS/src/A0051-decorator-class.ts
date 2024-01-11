export class Animal {
    constructor(public cor: string) {}
}

function decorator(target: any): any {
    console.log('decorator');
    return target;
}

const AnimalDecorated = decorator(Animal);
const animal = new AnimalDecorated('roxo');
console.log(animal);
