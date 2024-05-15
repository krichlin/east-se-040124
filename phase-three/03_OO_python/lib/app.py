#!/usr/bin/env python3
import ipdb; 

"""
Pet
    - name
    - age
    - breed
"""
#✅ 1. Create a Pet class

    #✅ 2. Instantiate a few pet instances in ipdb
    #✅ 2a. Compare the two pet instances to demonstrate they are not the same object
    
    #✅ 3. Demonstrate __init__
    #✅ 3a. Add parameters for attributes
    #✅ 3b. use dot notation to access their attributes
    #✅ 3c. update attributes with new values

    #✅ 4. Demonstrate INSTANCE methods
    #✅ 4a. Create a hello method that will print "Hello!"
    #✅ 4b. Create a print_pet_details function that will print the pet attributes
    #✅ 4c. Create a speak method that will print "Woof" for dogs and "Meow" for cats


#✅ 5. Set constraints for updating properties (attributes that are controlled by methods)
    #✅ 5a. Create Owner class
    #✅ 5b. Create get/set instance methods for name property
    #✅ 5c. Create constraint to make sure the name is of type string
    #✅ 5d. Compile get_name, set_name under the same property name (@ decorator is syntactic sugar)
    #✅ 5e. Add parameter to pass in name property value on instantiation
    #✅ 5f. Use the name property to set the name "private" attribute on instantiation
