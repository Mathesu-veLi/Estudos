type Pessoa = {
    nome: string;
    idade: Idade;
    salario: number;
    corPreferida?: string;
}
type Idade = number;
type CorRGB = 'Vermelho' | 'Verde' | 'Azul';
type CorCMYK = 'Ciano' | 'Magenta' | 'Amarelo' | 'Preto';
type CorPreferida = CorRGB | CorCMYK;

