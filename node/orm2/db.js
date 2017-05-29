
// Notes:
// https://github.com/dresende/node-orm2/wiki/

// Import
var orm = require('orm');
var uuid = require('uuid/v4');
var _ = require('lodash');

// setup models
function setup(db, cb) {
	// define uuid type
	db.defineType('uuid', {
		datastoreType: function(prop) {
			return 'TEXT';
		},
		valueToProperty: function(value, prop) {
			if (value) {
				return value;
			} else {
				return uuid();
			}
		},
		propertyToValue: function(value, prop) {
			if (value) {
				return value;
			} else {
				return uuid();
			}
		},
	});

	// define app set model
	var AppSet = db.define('appset', {
		id: {type: 'uuid', key: true},
	}, {

	});

	// define app model
	var App = db.define('app', {
		id: {type: 'uuid', key: true},
		name: {type: 'text'},
		url: {type: 'text'},
		auth: {type: 'text'},
	}, {

	});
	App.hasOne('appset', AppSet, {reverse: 'apps'});

	// define access token model
	var AccessToken = db.define('access', {
		id: {type: 'uuid', key: true},
		signature: {type: 'text', big: true},
		date: {type: 'date', time: true},
		expires: {type: 'date', time: true},
		is_active: {type: 'boolean', default: false},
	}, {

	});
	AccessToken.hasOne('appset', AppSet, {reverse: 'tokens'});

	return cb(null, db);
}

module.exports = function(cb) {
	orm.connect('sqlite:///Users/nicholaspiano/code/odin/odin.registry/node/db/db.sqlite3', function(err, db) {
		if (err) return cb(err);
		setup(db, cb);
	});
};