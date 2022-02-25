# Modifying professor code from week 1
import person_class 
import student

# Creating a person
sample_person = person_class.Person("Norton Juster", 10)
print(sample_person)
print(sample_person.get_name())
print(sample_person.get_age())

# Create a student object 
sample_student = student.Student("Dennis Ritchie", 16, "basketweaving", 11)
# Print attributes of the student object
print(sample_student)
print(sample_student.get_age())
print(sample_student.get_name())
print(sample_student.get_gradyear())
print(sample_student.get_major())
# Change major 
sample_student.set_major("biology")
# Change grad year
sample_student.set_gradyear(12)
# Print attributes of the student object
print(sample_student)