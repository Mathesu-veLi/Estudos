type Documento = {
    titulo: string;
    texto: string;
    data?: Date;
};

const documento: Documento = {
    titulo: 'O título',
    texto: 'O texto',
};

console.log(documento.data?.toDateString() ?? '1-Não existe data.');
console.log(undefined ?? '2-Não existe data.');
console.log(null ?? '3-Não existe data.');
console.log(false ?? '4-Não existe data.');
