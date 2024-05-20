#!/usr/bin/env python3
import ipdb; 

"""
SWABATs:
 - Create a new Python class
 - Pass new instances information during instantiation
 - Give our new class methods
 - Protect attributes with properties
"""
class Pet:
    def __init__(self, name="Pet", age=0, breed='Unknown'):
        self.name = name
        self.age = age
        self.breed = breed

    def hello(self):
        print('Hello')

    def speak(self):
        if self.breed == 'Dog':
            print('Bark')
        elif self.breed == 'Cat':
            print('Meow')
        else:
            print('...silence')

    def __repr__(self):
        return f'<Pet name={self.name}>'


class Owner:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        if type(new_name) == str:
            self._name = new_name
        else:
            raise TypeError('Name must be of type str')
    
    name = property(get_name, set_name)

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if isinstance(new_age, int):
            self._age = new_age
        else:
            raise TypeError('Age must be an integer')

    age = property(get_age, set_age)



class Person:
    def __init__(self, name='Jane Doe', age=0):
        self.name = name
        self.age = age
        self.hygiene = 10

    def workout(self, type_of_workout):
        decrement = 2
        if type_of_workout == 'Run':
            decrement = 5
         
        self.hygiene = self.hygiene - decrement
        self.print_current_hygiene()
        if self.hygiene < 4:
            print('Take a shower!')

    def take_shower(self):
        self.hygiene = 10
        self.print_current_hygiene()

    def print_current_hygiene(self):
        print(f"Your current hygiene is now {self.hygiene}")

    def get_age(self):
        return self._age
    
    def set_age(self, new_age):
        # if type(new_age) == int:
        if isinstance(new_age, int):
            if new_age > 12:
                self._age = new_age
            else:
                raise ValueError('Age must be greater than 12')
        else:
            raise TypeError('Age must be of type int')

    age = property(get_age, set_age)


ipdb.set_trace()