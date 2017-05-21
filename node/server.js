
var http = require('http');
var fs = require('fs');

var server = http.createServer(function (request, response) {

	// requests can come to:
	// 1. /a/<UUID> to specify an application to load.
	// 2. /api/<UUID> to establish a websocket connection for app configuration (does not load UI).
	// 3. /<ADMIN-UUID> to establish a websocket connection for admin CMS access.

	response.end(JSON.stringify({
		url: request.url,
		method: request.method,
	}));
});
server.listen(8080, function() {
	console.log('Server started.');
});