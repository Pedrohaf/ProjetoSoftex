const Sequelize = require('sequelize')

const sequelize = new Sequelize('cadastro', 'root', '123467', {
    host: 'localhost',
    dialect: 'mysql'
});

sequelize.authenticate()
.then(function(){
    console.log("Pegou")
}).catch(function(){
    console.log('Deu merda')
})

module.exports = sequelize;