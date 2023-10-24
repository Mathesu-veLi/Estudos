const express = require('express');
const route = express.Router();
const homeController = require('./src/controllers/homeController');
const contatoController = require('./src/controllers/contatoController');

route.get('/', homeController.páginaInicial);
route.post('/', homeController.trataPost);

route.get('/contato', contatoController.páginaInicial);

module.exports = route;