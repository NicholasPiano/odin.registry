
// Notes:
// https://github.com/dresende/node-orm2/wiki/

// Import
var orm = require('orm');
var uuid = require('uuid');
var _ = require('lodash');
var database = require('./db.js');

// setup
database(function (err, db) {
	db.drop(function (err) {
		db.sync(function (err) {

			// 1. create app set
			db.models.appset.create({}, function (err, appset) {

				// 2. create apps
				new Promise(function(resolve, reject) {

					// main app
					db.models.app.create({
						name: 'main',
						url: 'ws://localhost:8000',
						auth: 'ws://localhost:8080',
					}, function (err, app) {
						app.setAppset(appset, function (err) {});
					});

					// chat app
					db.models.app.create({
						name: 'chat',
						url: 'ws://localhost:8081',
						auth: 'ws://localhost:8080',
					}, function (err, app) {
						console.log(app.setAppset);
						app.setAppset(appset, function (err) {});
					});

					resolve();
				}).then(function () {
					db.close();
				});
			});
		});
	});
});