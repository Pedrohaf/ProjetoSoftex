const express = require('express')
const app = express()

const db = require('./bd')

app.get('/', async (req, res) => {
    res.send('Pagina inicial')
});

app.listen(8080)