# What things do people have?
# - Private attributes: name, age
# - init function
# - Print an object as a string __str__ method

# - Add a get method for each attribute
# - Add a set attribute for each attribute (name can't be blank, age must be greater than 0)
# - Enhance the driver program to call and validate the operation of each method just added

import random 

class Person:

    # class variables shared by all people
    scientific = 'homo sapiens'
    hobbies = []

    def __init__(self, fname="Nomen", lname="Nescio"):
        self.__first_name = fname
        self.__last_name = lname
        self.__age = random.randrange(1,99)
        # From lecture 
        if random.randint(0,1) == 0:
            self.__favorite_soup = "Manhattan Clam Chowder"
        else:
            self.__favorite_soup = "Boston Clam Chowder"
    
    def get_age(self):
        return self.__age 
    
    def get_name(self):
        return("%s %s" % (self.__first_name, self.__last_name))
    
    def get_favorite_soup(self):
        return self.favorite_soup 

    def add_hobby(self, hobby):
        if len(hobby) > 0:
            self.hobbies.append(hobby) 
    
    def change_firstname(self, newname):
        if len(newname) > 0:
            self.__first_name = newname 
    
    def change_lastname(self, newname):
        if len(newname) > 0:
            self.__last_name = newname 
            
    def __str__(self):
        return("Person is name %s %s and is %d with hobbies: %s" % (self.__first_name, self.__last_name, self.__age, str(self.hobbies)))
    