#!/usr/bin/env python3
from models.pet import Pet

class Owner:
    def __init__(self, name, age, experience=0):
        self.name = name
        self.age = age
        self.experience = experience

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int):
            self._age = new_age
        else:
            raise TypeError('Age must be an integer')


    def __repr__(self):
        return f'<Owner name={self.name} >'
