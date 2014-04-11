PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE login(
usn text primary key,
password text not null
);
INSERT INTO "login" VALUES('1PI11CS054','welcome');
INSERT INTO "login" VALUES('1PI11CS034','welcome');
INSERT INTO "login" VALUES('1PI11CS010','welcome');
INSERT INTO "login" VALUES('1PI11CS050','welcome');
INSERT INTO "login" VALUES('1PI11CS020','welcome');
COMMIT;
