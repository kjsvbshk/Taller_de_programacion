const express = require('express');
const dotenv = require('dotenv');

dotenv.config();
const app = express(); 

const port = process.env.PORT || 3000;

const routerApi = require('./routes');

app.use(express.json());

app.get('/', (req,res) => {
    res.send('Welcome to the jungle');
}); 

routerApi(app);

app.listen(port,()=>{
    console.log("Port ==> ", port);
});