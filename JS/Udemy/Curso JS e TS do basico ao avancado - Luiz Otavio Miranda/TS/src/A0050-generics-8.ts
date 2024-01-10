const objeto1: Record<string, string | number> = {
    nome: 'Matheus',
    sobrenome: 'Levi',
    idade: 13,
};
console.log(objeto1);

export type PessoaProtocol = {
    nome?: string;
    sobrenome?: string;
    idade?: number;
};

type PessoaRequired = Required<PessoaProtocol>;

type PessoaPartial = Partial<PessoaRequired>;

type PessoaReadonly = Readonly<PessoaRequired>;

type PessoaPick = Pick<PessoaRequired, 'nome' | 'sobrenome'>;

const objeto2: PessoaProtocol = {
    nome: 'Matheus',
    sobrenome: 'Levi',
    idade: 13,
};
console.log(objeto2);

type ABC = 'A' | 'B' | 'C';
type CDE = 'C' | 'D' | 'E';
type TipoExclude = Exclude<ABC, CDE>;
type TipoExtract = Extract<ABC, CDE>;
