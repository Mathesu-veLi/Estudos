const texto = `João trouxe flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.

Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente. Maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!`;

const arquivos = [
  'Atenção.jpg',
  'FOTO.jpeg',
  'Meu gatinho.jpg',
  'Meu gatinho.JPG',
  'Meu gatinho.JPEG',
  'Marido.png',
  'lista de compras.txt',
];

const cpfs = `
Os CPFs são:
906.745.435a-48
a209.721.825-35
875.370.505-03

401.302.655.43
`;

const ips = `
Os IPs são:
0.0.0.0

242.28.57.131 123.115.95.188 52.177.98.235
71.151.171.10

255.255.255.255

300.255.255.300

`;

const alfabeto =
  'ABCDEFGHIJKLMNPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 0123456789';

const html = '<p>Olá mundo</p> <p>Olá de novo</p>';
const html2 = `<p
class="teste teste"
data-teste='teste'>
  Olá mundo
</p> <p>Olá mundo</p> <div>Sou a div</div>`;

const lookahead = `ONLINE 192.168.0.1 ABCDEF inactive
OFFLINE 192.168.0.2 ABCDEF active
ONLINE 192.168.0.3 ABCDEF active
ONLINE 192.168.0.4 ABCDEF active
OFFLINE 192.168.0.5 ABCDEF active
OFFLINE 192.168.0.6 ABCDEF inactive`;

module.exports = {
  texto,
  arquivos,
  html,
  html2,
  alfabeto,
  cpfs,
  ips,
  lookahead,
};
