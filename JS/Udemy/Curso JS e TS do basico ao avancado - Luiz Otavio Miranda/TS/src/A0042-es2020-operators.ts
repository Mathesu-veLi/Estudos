type Documento = {
    titulo: string;
    texto: string;
    data?: Date;
};

const documento: Documento = {
    titulo: 'O título',
    texto: 'O texto',
};

console.log(documento.data?.toDateString());
