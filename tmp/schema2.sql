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
CREATE TABLE names(
usn text primary key,
name text
);
INSERT INTO "names" VALUES('1PI11CS054','Deepak Karki');
INSERT INTO "names" VALUES('1PI11CS034','Arjun singhvi');
INSERT INTO "names" VALUES('1PI11CS010','Aslum Bhai');
INSERT INTO "names" VALUES('1PI11CS050','Daewood Ibrahim');
INSERT INTO "names" VALUES('1PI11CS020','Dhanya Bharadwaj');
COMMIT;
