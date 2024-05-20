# OOP 2: Class Methods & Class Variables

## SWBATs

- [ ] Demonstrate Decorators 
    - [ ] `@decorator`
- [ ] Demonstrate class variables
    - [ ] Defining class variables
    - [ ] Updating class variables 
- [ ] Demonstrate class methods
    - [ ] Defining class methods 
    - [ ] `@classmethod`
    - [ ] `cls keyword`
- [ ] Object Inheritance
- [ ] Stretch Goals
    - [ ] Super
    - [ ] Creating a decorator

---

## Deliverables

#### 1. Import the Pet and Owner class to use in debug.py
##### 1a. Create a few Pet and Owner instances
<br />

#### 2. Keep track of the total number of Pets created
##### 2a. Create a class attribute
##### 2b. Update class attribute whenever an instance is initialized
##### 2c. Create a class method increase_pets that will increment total_pets
##### 2d. Create a class attribute for all pet instances
##### 2c. Create a class method add_new_pet that will add pet instance to all list
<br />

#### 3. Demonstrate inheritance with Owner and Person classes
##### 3a. Remove the __init__ from Owner class
<br />

#### 4. Create a subclass of Pet called Cat
##### 4a. Create an __init__ method that has all parameters of Pet including an additional parameter: indoor
##### 4b. Use super to pass Pet parameters to super class
##### 2d. Update the instance in debug.py to rose = Cat('rose', 11, 'domestic longhair', True)
<br />

#### 5. Create a method unique to the Cat subclass called talk which returns the string "Meowwwwwww"
<br />

#### 6. Demonstrate First Class Functions
##### 6a. Create functions to be used as callbacks 
##### 6b. Create a higher-order function that will take a callback as an argument
<br />

#### 7. Higher order functions
##### 7a. Create a higher-order function that returns a function
<br />

#### 8. Create a higher-order function that returns two functions
<br />

#### 9. Demonstrate how to create a decorator.  Create a function that...
##### 9a. takes a function as an argument, 
##### 9b. has an inner function, and 
##### 9c. returns the inner function
<br />

#### 10. property decorator
