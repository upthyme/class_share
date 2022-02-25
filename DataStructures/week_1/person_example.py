import person_class 

# Creating a person
sample_person = person_class.Person("Norton", "Juster")
print(sample_person)
print(sample_person.get_name())
print(sample_person.get_age())
print(sample_person.get_favorite_soup())

noname_person = person_class.Person()
print(noname_person)
noname_person.add_hobby("brushing teeth")
noname_person.add_hobby("walking around town")
noname_person.change_firstname("George")
noname_person.change_lastname("Forman")
print(noname_person)
