#!/usr/bin/env python3
import ipdb

pet_mood = 'Hungry!'
pet_name = 'Apollo'

print(f"Formatted String")

#✅ 1. Create a condition to check a pet's mood
    # If "pet_mood" is "Hungry!", "Rose needs to be fed."

# if pet_mood == "Hungry!":
#     print(f"{pet_name} needs to be fed.")
# elif pet_mood == "Rowdy!":
#     print(f"{pet_name} needs a walk.")
# else:
#     print(f"{pet_name} is all good.")

    # If "pet_mood" is "Rowdy!", "Rose needs a walk."
    # In all other cases, "Rose is all good."

#✅ 2. Create a ternary operator using "pet_mood" as a condition:

ternary = f"{pet_name} needs to be fed." if pet_mood == 'tired!' else f"{pet_name} is all good."
print(ternary)

#✅ 3. Create a function (say_hello) that returns the string "Hello, world!"

def say_hello(parameter='default'):
    return "Hello, world!"

print(say_hello(pet_name))

#✅ 4. Create a function (pet_greeting) that will return a string with interpolated pet's name

def pet_greeting(pet_name):
    return f"Hello {pet_name}"

print(pet_greeting("Daisy"))

#✅ 5. Move conditional logic from Deliverable 1 into a function (pet_status) so that we may use it with different pets / moods

def pet_status(pet_mood='Good!', pet_name='Joe'):
    if pet_mood == "Hungry!":
        print(f"{pet_name} needs to be fed.")
    elif pet_mood == "Rowdy!":
        print(f"{pet_name} needs a walk.")
    else:
        print(f"{pet_name} is all good.")

pet_status(pet_name='Apollo')

#✅ 6. Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
    # If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
    # pet_birthday(10) => "Happy Birthday! Your pet is now 11."
    # pet_birthday("oops") => "Type Error Occurred"

def pet_birthday(age=0):
    try:
        age += 1
        return f"Happy Birthday! Your pet is now {age}."
    except TypeError:
        print('Type error: must be an int')
    except NameError:
        print('Name error')

print(pet_birthday(10))