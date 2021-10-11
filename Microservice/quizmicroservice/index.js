const mysql = require("mysql");
const express = require("express");
var app = express();
const bodyparser = require('body-parser');
const cors = require('cors');

app.use(bodyparser.json());
app.use(cors());

var mysqlConnection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'root',
    database: 'quiz',
})

mysqlConnection.connect((err) => {
    if (!err)
    console.log("win")
    else
    console.log("fail " + JSON.stringify(err, undefined, 2))
})

app.listen(3003,()=>console.log('running'))

app.get('/quiz', (req,res)=>{
    mysqlConnection.query('SELECT * FROM quiz', (err, rows, fields)=>{
        if(!err)
        res.json(rows)
        else
        console.log(err)
    })
})