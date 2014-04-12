PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;
CREATE TABLE student_names(
usn text primary key,
name text
);
INSERT INTO "student_names" VALUES('1PI11CS001','Aashish');
INSERT INTO "student_names" VALUES('1PI11CS002','Ajay');
INSERT INTO "student_names" VALUES('1PI11CS003','Angad');
INSERT INTO "student_names" VALUES('1PI11CS004','Chitra');
INSERT INTO "student_names" VALUES('1PI11CS005','Deepak');
CREATE TABLE student_login(
usn text primary key,
password text,
foreign key (usn) references student_names(usn)
);
INSERT INTO "student_login" VALUES('1PI11CS001','welcome');
INSERT INTO "student_login" VALUES('1PI11CS002','welcome');
INSERT INTO "student_login" VALUES('1PI11CS003','welcome');
INSERT INTO "student_login" VALUES('1PI11CS004','welcome');
INSERT INTO "student_login" VALUES('1PI11CS005','welcome');
CREATE TABLE teacher_names(
tid text primary key,
name text
);
INSERT INTO "teacher_names" VALUES('TEACH-001','Anand');
INSERT INTO "teacher_names" VALUES('TEACH-002','Goyel');
INSERT INTO "teacher_names" VALUES('TEACH-003','Arjun');
CREATE TABLE teacher_login(
tid text primary key,
password text,
foreign key (tid) references teacher_names(tid)
);
INSERT INTO "teacher_login" VALUES('TEACH-002','password');
INSERT INTO "teacher_login" VALUES('TEACH-001','password');
INSERT INTO "teacher_login" VALUES('TEACH-003','password');
CREATE TABLE teacher_lab(
tid text primary key,
lab text,
foreign key (tid) references teacher_names(tid)
);
INSERT INTO "teacher_lab" VALUES('TEACH-001','11CS351');
INSERT INTO "teacher_lab" VALUES('TEACH-002','11CS352');
INSERT INTO "teacher_lab" VALUES('TEACH-003','11CS353');
CREATE TABLE lab_names(
sid text primary key,
name text
);
INSERT INTO "lab_names" VALUES('11CS351','COMPILERS');
INSERT INTO "lab_names" VALUES('11CS352','COMPUTER-NETWORKS');
INSERT INTO "lab_names" VALUES('11CS353','ALGORITHMS');
CREATE TABLE student_lab(
usn text,
lab text,
foreign key (usn) references student_names(usn)
);
INSERT INTO "student_lab" VALUES('1PI11CS001','11CS351');
INSERT INTO "student_lab" VALUES('1PI11CS001','11CS352');
INSERT INTO "student_lab" VALUES('1PI11CS001','11CS353');
INSERT INTO "student_lab" VALUES('1PI11CS002','11CS352');
INSERT INTO "student_lab" VALUES('1PI11CS002','11CS353');
INSERT INTO "student_lab" VALUES('1PI11CS003','11CS351');
INSERT INTO "student_lab" VALUES('1PI11CS003','11CS352');
INSERT INTO "student_lab" VALUES('1PI11CS003','11CS353');
INSERT INTO "student_lab" VALUES('1PI11CS004','11CS351');
INSERT INTO "student_lab" VALUES('1PI11CS004','11CS352');
INSERT INTO "student_lab" VALUES('1PI11CS005','11CS351');
INSERT INTO "student_lab" VALUES('1PI11CS005','11CS352');
INSERT INTO "student_lab" VALUES('1PI11CS005','11CS353');
COMMIT;
