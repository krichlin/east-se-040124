from models.appointment import Appointment

class Pet:
    all = []

    def __init__(self, name="Pet", age=0, breed='Unknown', owner=None):
        self.name = name
        self.age = age
        self.breed = breed
        self.owner = owner

        Pet.add_new_pet(self)

    @classmethod
    def add_new_pet(cls, new_pet):
        cls.all.append(new_pet)

    @classmethod
    def total_count(cls):
        return len(cls.all)

    def speak(self):
        if self.breed == 'Dog':
            print('Bark')
        elif self.breed == 'Cat':
            print('Meow')
        else:
            print('...silence')

    def appointments(self):
        return [appointment for appointment in Appointment.all if appointment.pet == self]

    def procedures(self):
        return [appointment.procedure for appointment in self.appointments()]

    def __repr__(self):
        return f'<Pet name={self.name} owner={self.owner}>'
