let num = [5, 8, 4]
num.push(7)
num[4] = 3

console.log(`Nosso vetor é o ${num}`)

num.sort()
console.log(`Esse vetor de ${num.length} números, com os números em ordem crescente fica: ${num}`)

/*for (let c = 0; c <= num.length; c++) {
    console.log(num[c])
}*/

for(let c in num)
{
    console.log(num[c])
}

console.log(`O valor 7 está na posição ${num.indexOf(7)}`)
if (num.indexOf(1) == -1)
{
    console.log('O valor 1 não foi encontrado')
} else
{
    console.log(`O valor 1 está na posição ${num.indexOf(1)}`)
}