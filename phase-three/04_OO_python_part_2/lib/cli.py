import ipdb
from models import Owner

if __name__ == '__main__':
    name = input('What is your name?')
    age = input('What is your age?')
    new_owner = Owner(name=name, age=int(age))
    print(f'Welcome {new_owner.name}')
    print("Please select an option:")
    print('1. Create new pet')
    option = input('Which menu option?')

    if option == '1':
        pet_name = input("What is your pet's name?")
