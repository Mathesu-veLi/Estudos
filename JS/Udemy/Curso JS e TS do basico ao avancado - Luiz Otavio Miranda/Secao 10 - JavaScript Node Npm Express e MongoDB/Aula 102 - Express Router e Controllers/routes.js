const express = require('express');
const route = express.Router();
const homeController = require('./controllers/homeController');
const contatoController = require('./controllers/contatoController');

route.get('/', homeController.páginaInicial);
route.post('/', homeController.trataPost);

route.get('/contato', contatoController.páginaInicial);

module.exports = route;