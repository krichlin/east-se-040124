DROP TABLE IF EXISTS owners;

CREATE TABLE IF NOT EXISTS owners(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    experience INTEGER
);

INSERT INTO owners (name, age, experience) VALUES
('Emiley', 29, 5),
('Carisa', 23, 3),
('Kailey', 23, 3);

SELECT * FROM owners;

SELECT name FROM owners;

SELECT * FROM owners
WHERE id = 3;

SELECT name FROM owners
WHERE age > 23;

UPDATE owners SET age = 29
WHERE id = 1;

UPDATE owners
SET age = 24
WHERE id IN (2,3);
-- WHERE id=2 OR id=3

DELETE FROM owners
WHERE id=2;