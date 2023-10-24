const números = [1, 2, 3, 4, 5, 6, 7, 8, 9];

for (let número of números) {
    if (número === 3) {
        console.log('Pulei o número 3')
        continue;
    }
    
    console.log(número);
    if (número === 7) {
        console.log('Irei parar aqui no 7 mesmo')
        break;
    }
}