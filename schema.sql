drop table if exists login;
create table login (
  usn text primary key,
  password text not null
);
