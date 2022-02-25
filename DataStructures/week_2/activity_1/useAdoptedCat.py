import AdoptedCat 

testkitty = AdoptedCat.AdoptedCat("Felix", 10, "Rosemary")
testkitty.meow() # using a method from the parent 
print(testkitty.getOwner()) 
print(testkitty) 

# Changing things 
testkitty.setOwner("Heather")
testkitty.haveBirthday()
print(testkitty.getOwner())
print(testkitty)