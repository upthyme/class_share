# Modifying professor code from week 1

class Person:

    def __init__(self,n,a):
        self.__name = n
        self.__age = a

    def __str__(self):
        return(self.__name + " is "+ str(self.__age) + " years old.")

    def get_name(self):
        return(self.__name)

    def get_age(self):
        return(self.__age)

    def set_name(self,n):
        if len(n)>0:
            self.__name = n

    def set_age(self,a):
        if a > 0:
            self.__age = a
