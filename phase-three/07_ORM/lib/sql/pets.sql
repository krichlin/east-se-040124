DELETE FROM pets;

CREATE TABLE IF NOT EXISTS pets(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    breed TEXT,
    owner_id INTEGER
);

INSERT INTO pets (name, age, breed, owner_id)
VALUES ('Apollo', 2, 'Dog', 1),
('Dayna', 3, 'Dog', 3),
('John Ham', 1, 'Hamster', 1),
('Nymeria', 1, 'Hamster', 1);
