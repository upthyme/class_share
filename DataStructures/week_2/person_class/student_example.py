# Modifying professor code from week 1
import student

"""
# Part 1
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
"""

s1 = student.Student("Dennis", 16, "art", 11)
s2 = student.Student("Mick", 16, "psychology", 12)
s3 = student.Student("Mick", 16, "psychology", 12)

print(s1==s2) # False 
print(s2==s3) # True
