# Sequence Types
# docs: 
# https://docs.python.org/3/tutorial/datastructures.html
import ipdb

#lists, tuples, dictionaries, and sets are all individual data types that are used to store collections of data.  they each have their own unique properties/behaviors.  a lot of those behaviors overlap

# Creating Lists
#✅ 1. Create a list of 10 pet names


#------------------------ Reading Information from Lists
#✅ 1a. Return the first pet name 


#✅ 1b. Return the last value


#✅ 1c. Return all pet names beginning from the 3rd index


#✅ 1d. Return all pet names before the 3rd index



#✅ 1e. Return all pet names beginning from the 3rd index and up to (exclusive of) the 7th


#✅ 1f. Find the index of a given element


#✅ 1g. Reverse the original list
# mutate our list, destructive
# does not return anything


#✅ 1h. Return the frequency of a given element 


#---------------------------------- Updating Lists
#✅ 1i. Change the first element to all uppercase


#---------------------------------- Adding items to list
#✅ 1j. Append a new name to the list


#✅ 1k. Add a new name at a specific index


#✅ 1l. Add two lists together 

#---------------------------------- Removing 
#✅ 1m. Removes and returns the final element from the list
 

#✅ 1n. Remove element by specific index


#✅ 1o. Remove a the first instance of a specific element 


#✅ 1p. Remove all pet names from the list

#---------------------------------- Tuple 
# can't mutate tuples
# can have repeats
#🛑 Using a trailing comma for a singleton tuple: a, or (a,)
#✅ 2. Create a Tuple of pet 10 ages 



#✅ 2a. Print the first pet age


#---------------------------------- Testing Changeability 
#✅ 2b. Attempt to remove an element with .pop (should error)


#✅ 2c. Attempt to change the first element (should error)


#---------------------------------- Tuple Methods
#✅ 2d. Return the frequency of a given element


#✅ 2e. Return the index of first matching element 


#---------------------------------- Demo Sets
#✅ 3. Create a set of 3 pet foods


# Demo Dictionaries 
#---------------------------------- Creating 
#✅ 4. Create a dictionary of pet information with the keys name, age and breed
# KEYS AS STRINGS


#✅ 4a.  Use dict to create a dictionary of pet information with the keys name, age and breed

#---------------------------------- Reading
#✅ 4b. Print the pet attribute of name using bracket notation

#✅ 4c. Print the pet attribute of age using .get


#---------------------------------- Updating 
#✅ 4d. Update the pets age to 12


#✅ 4e. Update the other pets age to 26


#---------------------------------- Deleting
#✅ 4f. Delete a pets age using the del keyword 


#✅ 4g. Delete the other pets age using the .pop, returns removed value


#✅ 4h. Delete the last item in the pet dictionary using popitem()

#✅ 5. loop through a range of 10 and print every number within the range


#✅ 5a. loop through a range between 50 and 60 that iterates by 2 and print every number
#range(start, stop, increment)


#✅ 5b. Loop through the pet_info list and print every dictionary  


#✅ 6. Create a function that takes a list as an argument. 
 

#✅ 7. Create a function that takes a list as an argument.(simple example) 



#✅ 8. Create a function that updates the age of a given pet
#replace_age(pet_info, "spot", 2) # => { 'name': "spot", 'age': 2, 'breed': "boxer"}
#replace_age(pet_info, "does_not_exist", 5) # => 'pet not found'


# map like 
#✅ 9. Use list comprehension to return a list containing every pet name from pet_info changed to uppercase


# find like
#✅ 9a. Use list comprehension to find a pet named spot


# filter like
#✅ 9b. Use list comprehension to find all of the pets under 3 years old
