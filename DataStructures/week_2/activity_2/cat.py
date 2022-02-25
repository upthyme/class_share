class Cat:
    def __init__(self, n, a):
        self.__name = n
        self.__age = a

    def __str__(self):
        return("My name is "+self.__name + 
        " and I am "+str(self.__age) + " years old")

    def meow(self):
        print(self.__name + " says 'Meow!'")

    def get_age(self):
        return(self.__age)

    def get_name(self):
        return(self.__name)

    def haveBirthday(self):
        self.__age += 1

    # Python magic functions 
    
    def __eq__(self,other):
        if self.__name == other.get_name() and self.__age == other.get_age():
            return True
        return False

    def __lt__(self,other):
        if self.__name < other.get_name():
            return True 
        elif self.__name == other.get_name():
            if self.__age < other.get_age():
                return True 
        return False
