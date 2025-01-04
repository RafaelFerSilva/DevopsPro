const express = require('express')
const app = express()

app.get('/', (req, res) => {
    res.json({application: "NodeJS Boilerplace" , versao: "1.0"})
})

app.listen(8080, () => console.log("Servido rodando na porta 8080"))