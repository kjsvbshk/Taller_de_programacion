const express = require('express'); 

const personsRouter = require('./persons.router');

function routerApi(app) {
  const router = express.Router();
  router.use('/persons', personsRouter);
  app.use('/api/v1', router); 
}

module.exports = routerApi;