# Object-Relational Mapping

## SWBATs

- [ ] Demonstrate configuring an application to connect with sqlite3
- [ ] Demonstrate a create table method 
- [ ] Review preventative measures for SQL injection
- [ ] Demonstrate a save and create methods  
    - [ ] Save => Persist created instance to DB
    - [ ] Create => Instantiate / persist created instance to DB, return new instance 
- [ ] Demonstrate query methods to find and retrieve resources 
- [ ] Stretch Goal
    - [ ] Make a “create_and_find_by” member
    - [ ] Make “update” and “delete” member

---

## Deliverables

`Pet.py:` 
#### 1. In `Pet.py` add "__init__" with "name", "species", "breed", "temperament", and "id" (Default: None) Attributes 
#### 2. Create table
#### 3. Drop table
#### 4. Insert instance into DB
#### 5. Initialize instance and insert into database
#### 6. Create instance from DB, thus getting the ID
#### 7. Get all rows
#### 8. Get row by name
#### 9. Get row by id
#### 10. Find row, otherwise create row
##### 10a. Search for pet
##### 10b. Insert pet if it does not exist
##### 10c. Return pet if it does exist
#### 11. Update row
<br />

`Owner.py:`
#### 12. Create table
#### 13. Drop table
#### 14. Insert row
##### 14a. Update instance with new row's id
#### 15. Get all rows
##### 15a. Create helper method to turn a row into an owner instance
#### 16. Get row by id
#### 17. Delete row by id
#### 18. Update row by id