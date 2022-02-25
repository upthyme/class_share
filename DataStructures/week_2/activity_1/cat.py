class Cat:
    
    def __init__(self, n, a):
        self.__name = n
        self.__age = a 

    def __str__(self):
        return("My name is " + self.__name + "and I am " + str(self.__age) + " years old")

    def meow(self):
        print(self.__name + "says 'Meow!'") 

    def haveBirthday(self):
        self.__age += 1 

