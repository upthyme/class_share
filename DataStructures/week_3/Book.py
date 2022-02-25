class Book:
    def __init__(self,t,a,p):
        self.title = t
        self.author = a
        self.pages = p
        self.read = 0

    def __str__(self):
        return("\""+self.title+"\", by"+ self.author)

    def setReadPages(self,r):
        self.read = r

    def percentRead(self):
        return(str(self.read/self.pages*100))+"%"