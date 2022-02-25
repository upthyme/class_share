import cat 

class AdoptedCat(cat.Cat):

    def __init__(self,n,a,o):
        super().__init__(n,a)
        self.__owner = o 

    def __str__(self):
        s = super().__str__()
        s += " and I was adopted by " + self.__owner
        return(s)

    def get_owner(self):
        return(self.__owner)

    def set_owner(self, new_owner):
        self.__owner = str(new_owner) 

    # Equal
    def __eq__(self, other): 
        if (self.get_name() == other.get_name() and self.get_age() == other.get_age() and self.get_owner() == other.get_owner()): # name, age, and owner must be the same for the objects to be equal  
            return True 
        return False 
    
    # Less or equal to 
    def __le__(self, other): 
        if (self.get_name() < other.get_name() or self.get_name() == other.get_name()): # compare cat name 
            return True 
        elif (self.get_owner() < other.get_owner() or self.get_owner() == other.get_owner()): # compare owner name 
            return True 
        elif(self.get_name() == other.get_name() and self.get_owner() == other.get_owner()): 
            if (self.get_age() < other.get_age() or self.get_age() == other.get_age()): # compare cat age if the owner and name are the same
                return True 
        return False 