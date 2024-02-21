DROP TABLE IF EXISTS user;

CREATE TABLE IF NOT EXISTS user (
    id integer PRIMARY KEY AUTOINCREMENT,
    username text not null,
    password text not null
);