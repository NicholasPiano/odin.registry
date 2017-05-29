
// Notes:
// https://github.com/dresende/node-orm2/wiki/

// Import
var orm = require('orm');
var uuid = require('uuid');
var _ = require('lodash');
var database = require('./db.js');

// open database
database(function (err, db) {
	db.models.appset.find({}, function (err, appset) {
		console.log(appset[0].id);
	});
	db.models.app.find({}, function (err, app) {
		if (err) throw err;
		app[0].getAppset(function (appset) {
			console.log(appset);
		});
		db.close()
	});
});