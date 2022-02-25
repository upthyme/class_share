import AdoptedCat 

c1 = AdoptedCat.AdoptedCat("Garfield",12, "Joe")
c2 = AdoptedCat.AdoptedCat("Nermal",2, "Joe")
c3 = AdoptedCat.AdoptedCat("Nermal",2, "Joe")
c4 = AdoptedCat.AdoptedCat("Garfield", 2, "Natalie")
c5 = AdoptedCat.AdoptedCat("Garfield", 3, "Adam")
c6 = AdoptedCat.AdoptedCat("Garfield", 5, "Adam")

print("Equality tests")
print(c1 == c2) # False
print(c3 == c2) # True

print("\nShow le")
print(c1 <= c2) # True 
print(c2 <= c1) # True, Nermal comes after Garfield BUT they share the same owner
print(c2 <= c4) # True, Nermal comes after Garfield BUT Joe comes before Natalie
print(c2 <= c5) # False, Nermal comes after Garfield AND Joe comes after Adam 
print(c2 <= c5) # False, Nermal comes after Garfield
print(c5 <= c6) # True 
print(c2 <= c3) # True because theyre the same 

print("\nShow ge which python infers (implements based on how we wrote le)")
print(c1 >= c2) # True, Joe is their owner  
print(c2 >= c1) # True 
