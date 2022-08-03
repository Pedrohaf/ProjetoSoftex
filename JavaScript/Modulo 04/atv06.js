let carro ={
    cor: 'Preto',
    marca: 'Fiat',
    ano: 2016
}

const array = [10, 20,30]

const forOf = () =>{
    console.log('Demonstrando o for of')
    console.log(' ')
    for(const e of array){
        console.log(e)
    }

}
console.log(' ')

const forIn = () =>{
    console.log('Demonstrando o for in')
    console.log(' ')
    for(const e in carro){
        console.log(e)
    }
}

console.log(forOf())
console.log(forIn())
