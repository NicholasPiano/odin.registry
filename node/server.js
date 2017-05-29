
// Notes:
// Router: https://www.npmjs.com/package/router
// Testing: localhost:8080/a/60cf1f0a-ff37-4ecb-abbf-b6745bce57a1

// Import
var http = require('http');
var fs = require('fs');
var Router = require('router');
var final = require('finalhandler');
var database = require('./db/db.js');

// Steps
// 1. create routers
var master = Router();

// a. basic application id response
var a = Router();
master.use('/a/', a);
a.get('/:uuid', function (request, response) {

	// params
	var uuid = request.params.uuid;

	// query database
	database(function (err, db) {
		response.statusCode = 200;
		response.setHeader('Content-Type', 'text/html; charset=utf-8');
		response.end(`
			<html>
				<head></head>
				<body>
					<div id="hook">${uuid}</div>
				</body>
			</html>
		`);
	});
});

// 2. create server
var server = http.createServer(function (request, response) {
	master(request, response, final(request, response));
});

// 3. start server
server.listen(8080, function() {
	console.log('Server started.');
});