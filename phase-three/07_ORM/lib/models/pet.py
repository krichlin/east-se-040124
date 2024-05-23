class Pet:

    def __init__(self, name="Pet", age=0, breed='Unknown', owner=None):
        self.name = name
        self.age = age
        self.breed = breed
        self.owner = owner

    def __repr__(self):
        return f'<Pet name={self.name} owner={self.owner}>'
