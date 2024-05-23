DELETE FROM owners;
DELETE FROM pets;


INSERT INTO owners (name, age, experience) VALUES
('Emiley', 29, 5),
('Carisa', 23, 3),
('Kailey', 23, 3);


INSERT INTO pets (name, age, breed, owner_id)
VALUES ('Apollo', 2, 'Dog', 1),
('Dayna', 3, 'Dog', 3),
('John Ham', 1, 'Hamster', 1),
('Nymeria', 1, 'Hamster', 1);
