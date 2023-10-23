const cpf = `
012.250.796-10
111.111.111-11
147.285.963-10
aaa.bbb.ccc-dd
`;

const regExCpf =
  /^(?!^(\d)\1{2}\.\1{3}\.\1{3}-\1{2}$)(\d{3}\.){2}\d{3}-\d{2}$/gm;

console.log(cpf.match(regExCpf));
