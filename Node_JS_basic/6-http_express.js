const express = require('express');
const app = express();

// Route principale
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Lancement du serveur
app.listen(1245);

module.exports = app;