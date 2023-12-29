function noReturn(...args: string[]): void {
    console.log(args.join(' '));
}

const person = {
    name: 'Matheus',
    lastName: 'Silva',

    showName(): void {
        console.log(this.name + ' ' + this.lastName);
    },
};

noReturn('Matheus', 'Levi');
person.showName();

export { person };
