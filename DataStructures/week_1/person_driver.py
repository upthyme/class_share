import Person

#first activity:
p1 = Person.Person("Kaya",22) #remember that the first Person is the name of the file; the second is the name of the class
print(p1)


#second activity:
print(p1.get_age()) #don't forget the ()s after the name of the function
print(p1.get_name())

p1.set_age(-2)
p1.set_name("")

print(p1)

p1.set_age(23)
p1.set_name("Kaya Lee")

print(p1)
