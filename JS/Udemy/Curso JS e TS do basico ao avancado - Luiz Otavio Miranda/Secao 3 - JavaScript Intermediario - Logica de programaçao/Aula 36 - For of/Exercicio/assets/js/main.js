const parágrafos = document.querySelector('.parágrafos');
const ps = parágrafos.querySelectorAll('p');

const estilosBody = getComputedStyle(document.body);

for (let i of ps){
    i.style.backgroundColor = estilosBody.backgroundColor;
    i.style.color = 'white';
}