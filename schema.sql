
--DROP TABLE IF EXISTS users;

CREATE TABLE users(
    id serial primary key,
    name varchar(32),
    email varchar(320),
    phone varchar(20),
    pin varchar(10),
    want2volunteer boolean,
    want2donate integer default 0,
    donated integer,
    signed timestamp default now()
);