const express = require('express');
const router = express.Router(); 

const personsController = require('../controllers/persons.controller');

router
    .get('/', personsController.getUsers )
    .get('/:id', personsController.getUserById )
    .post('/', personsController.createUser )
    .put('/:id', personsController.updateUser )
    .delete('/:id', personsController.deleteUser );

module.exports = router;