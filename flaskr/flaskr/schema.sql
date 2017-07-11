DROP TABLE IF EXISTS entries;
CREATE TABLE entries (
    id integer PRIMARY KEY autoincrement,
    title text not null,
    'text' text not null
);