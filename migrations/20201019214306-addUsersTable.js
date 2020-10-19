'use strict';

var dbm;
var type;
var seed;

/**
 * We receive the dbmigrate dependency from dbmigrate initially.
 * This enables us to not have to rely on NODE_PATH.
 */
exports.setup = function (options, seedLink) {
  dbm = options.dbmigrate;
  type = dbm.dataType;
  seed = seedLink;
};

exports.up = function (db) {
  return db.createTable('users', {
    id: { type: 'int', primaryKey: true, autoIncrement: true },
    first_name: 'string',
    last_name: 'string',
    email: { type: 'string', required: true },
    password: { type: 'string', required: true },
  });
};

exports.down = function (db) {
  return db.dropTable('users');
};

exports._meta = {
  version: 1,
};
