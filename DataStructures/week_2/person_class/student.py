import person_class

class Student(person_class.Person): 
    
    def __init__(self, n, a, m, g): 
        super().__init__(n,a)
        self.__major = m 
        self.__gradyear = g 

    def __str__(self): 
        string = super().__str__()
        string += " My major is " + str(self.__major) + ". Im in year " + str(self.__gradyear)
        return(string)

    def set_major(self,m):
        self.__major = m 

    def set_gradyear(self,g):
        self.__gradyear = g

    def get_major(self):
        return(self.__major)

    def get_gradyear(self):
        return(self.__gradyear)

    def __eq__(self,other):
        if(super().get_name() == other.get_name()): 
            return True 
        return False