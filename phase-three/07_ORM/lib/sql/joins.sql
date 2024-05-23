-- SELECT pets.name, owners.name FROM pets
-- JOIN owners ON pets.owner_id = owners.id;
-- WHERE pets.id = 1;

-- owner and all of their pets
-- SELECT * FROM owners
-- JOIN pets ON pets.owner_id = owners.id
-- WHERE owners.id = 1;

SELECT * FROM pets
JOIN owners ON pets.owner_id = owners.id
WHERE owners.id = 1;