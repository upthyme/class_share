import cat 

class AdoptedCat(cat.Cat):

    def __init__(self, n, a, o):
        super().__init__(n, a)
        self.__owner = o

    def __str__(self):
        s = super().__str__()
        s += " and I was adopted by " + self.__owner 
        return(s)
    
    def getOwner(self):
        return(self.__owner)

    def setOwner(self, new_owner):
        self.__owner = str(new_owner) 
