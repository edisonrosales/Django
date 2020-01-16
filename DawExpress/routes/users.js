var express = require('express');
var mysql = require('mysql');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
    res.json({ users: [{ name: 'Timmy' }] });
});

module.exports = router;

var connection = mysql.createConnection({ //Poner aqui todos los datos de conexion
    host: 'localhost',
    user: 'root',
    password: 'rootpass1',
    database: 'syscompsadb',
    port: '3306'
});

connection.connect();

//Colocar aqui una query para probar la conexion con la base de datos de mysql de Django
connection.query('select * from Empleado;', function(err, rows, fields) {
    if (err) throw err;
    console.log('The solution is: ', rows[0].Cedula);
});

connection.end();