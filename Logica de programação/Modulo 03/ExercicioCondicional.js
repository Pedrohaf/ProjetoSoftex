// definindo Propiedades do veiculo 
const quantRodas = 4
const peso = 2000
const quantPessoas = 5

// Condição para Habilitação tipo A
if (quantRodas == 2 | quantPessoas == 3){
    console.log('Abilitação indicada: tipo A')
}

// Condição para Habilitação tipo B
if (quantPessoas == 4 & quantPessoas <= 8 & peso <= 3500){
    console.log('Abilitação indicata: tipo B')
}

// Condição para Habilitação tipo C
if (quantRodas >= 4 ){
    if(peso >= 3500 & peso <= 6000){
        console.log('Abilitação inidicada: tipo C')
    }
}

// Condição para Habilitação tipo D
if(quantRodas >=4 & quantPessoas > 8){
    console.log('Abilitação indicada: tipo D')
}

// Condição para Habilitação tipo E
if(quantRodas>=4 & peso > 6000){
    console.log('Abilitação inidcada: tipo E')
}